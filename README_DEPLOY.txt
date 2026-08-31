TOEIC AI Tutor - Render 인터넷 배포용

1. 이 ZIP의 파일을 GitHub 새 저장소에 업로드
2. render.com 가입 → New → Web Service → GitHub 저장소 연결
3. Build Command: pip install -r requirements.txt
4. Start Command: python server.py
5. Render 서비스 Environment에 OPENAI_API_KEY 추가
6. Deploy 완료 후 https://xxxxx.onrender.com 주소로 접속

절대 API 키를 GitHub 파일 안에 넣지 마세요.

무료 Render Web Service는 15분 동안 요청이 없으면 잠들고,
다음 접속 때 다시 켜지는 데 시간이 걸릴 수 있습니다.

현재 학습 기록은 브라우저 localStorage에 저장되므로
집 PC와 휴대폰 기록은 서로 자동 동기화되지 않습니다.
기기 간 기록 동기화까지 원하면 로그인/DB 기능을 추가해야 합니다.
