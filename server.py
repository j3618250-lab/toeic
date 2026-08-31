import json, os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from openai import OpenAI

PORT=int(os.getenv("PORT","10000"))
MODEL=os.getenv("OPENAI_MODEL","gpt-5.6-luna")
SYSTEM = "너는 한국인 TOEIC 학습자를 위한 AI 문법 과외 선생님이다. 현재 문제와 최근 오답 기록을 바탕으로 TOEIC Part 5 관점에서 설명한다. 자동사/타동사, 1~5형식, 전치사, 복합명사, 수일치, 시제, 가산/불가산을 다룬다. 정답 근거, 오답 근거, 문장 구조, 패러프레이징, 연어, 시험 함정, 비교 예문을 구체적으로 한국어로 설명하라."

class Handler(SimpleHTTPRequestHandler):
    def _json(self, code, obj):
        data=json.dumps(obj,ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Content-Length",str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/",""):
            self.send_response(302)
            self.send_header("Location","/toeic_ai_tutor.html")
            self.end_headers()
            return
        return super().do_GET()

    def do_POST(self):
        try:
            if self.path not in ("/api/tutor","/api/generate"):
                return self._json(404,{"error":"API 경로를 찾을 수 없습니다."})
            key=os.environ.get("OPENAI_API_KEY")
            if not key:
                return self._json(500,{"error":"OPENAI_API_KEY가 서버 환경변수에 설정되지 않았습니다."})
            client=OpenAI(api_key=key)
            n=int(self.headers.get("Content-Length","0"))
            body=json.loads(self.rfile.read(n) or b"{}")

            if self.path=="/api/tutor":
                prompt="학습자 질문:\n"+body.get("message","")+"\n\n학습 맥락(JSON):\n"+json.dumps(body.get("context",{}),ensure_ascii=False)
                r=client.responses.create(model=MODEL,instructions=SYSTEM,input=prompt)
                return self._json(200,{"reply":r.output_text})

            schema="최근 오답을 바탕으로 TOEIC Part 5 문제 5개를 생성하라. JSON 배열만 출력하라. 각 객체는 id,type,category,q,choices,answer,tags,ex 키를 가진다. type은 intransitive/transitive/verb-form/compound-noun/agreement/tense/countability 중 하나. choices는 4개, answer는 0~3 정수. ex는 structure,prep,para,coll,trap,examples를 모두 포함한다. 정답은 하나만 명확해야 한다."
            prompt=schema+"\n\n학습 맥락:\n"+json.dumps(body.get("context",{}),ensure_ascii=False)
            r=client.responses.create(model=MODEL,instructions=SYSTEM,input=prompt)
            text=r.output_text.strip()
            if text.startswith("```"):
                text=text.split("\n",1)[1].rsplit("```",1)[0]
            return self._json(200,{"questions":json.loads(text)})
        except Exception as e:
            return self._json(500,{"error":str(e)})

if __name__=="__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"TOEIC AI Tutor running on 0.0.0.0:{PORT}")
    ThreadingHTTPServer(("0.0.0.0",PORT),Handler).serve_forever()
