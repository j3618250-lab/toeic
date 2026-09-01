import json, re
from pathlib import Path

ROOT=Path(__file__).parent
# word, Korean meaning, POS, completed TOEIC-style sentence, full Korean translation, memory point
V=[
('lodging','숙박 시설','n','The conference fee includes lodging for two nights.','회의 참가비에는 이틀간의 숙박이 포함된다.','lodging expenses / overnight lodging'),
('accommodation','숙박 시설; 편의 시설','n','The hotel can provide accommodation for up to 200 guests.','그 호텔은 최대 200명의 투숙객에게 숙박 시설을 제공할 수 있다.','provide accommodation for'),
('vacancy','공석; 빈방','n','The company posted a vacancy in its accounting department.','회사는 회계 부서의 공석을 공고했다.','fill a vacancy / job vacancy'),
('opening','공석; 시작','n','There are several openings for experienced technicians.','경력 기술자를 위한 공석이 여러 개 있다.','job opening'),
('depart','출발하다','v','The express train will depart from Platform 6 at noon.','급행열차는 정오에 6번 승강장에서 출발할 것이다.','depart from + 장소'),
('through','~을 통하여; 끝까지','prep','Please submit the application through the online portal.','온라인 포털을 통해 지원서를 제출해 주세요.','through + 수단/경로'),
('corporate','기업의','adj','All employees must follow the corporate travel policy.','모든 직원은 회사 출장 규정을 따라야 한다.','corporate policy / corporate headquarters'),
('bring back','되돌려 놓다; 다시 가져오다','v','The new campaign is expected to bring back former customers.','새 캠페인은 이전 고객들을 다시 돌아오게 할 것으로 예상된다.','bring back customers'),
('tricky','까다로운','adj','Negotiating the revised contract may be tricky.','수정된 계약을 협상하는 일은 까다로울 수 있다.','a tricky problem/situation'),
('charitable','자선의','adj','The firm made a charitable donation to the local shelter.','그 회사는 지역 보호소에 자선 기부를 했다.','charitable donation / organization'),
('disagreement','의견 차이; 불일치','n','A disagreement over the budget delayed the project.','예산에 관한 의견 차이로 프로젝트가 지연되었다.','a disagreement over/about'),
('for-profit company','영리 기업','n','The museum is operated by a for-profit company.','그 박물관은 영리 기업이 운영한다.','for-profit ↔ nonprofit'),
('logistical','물류의; 실행 계획상의','adj','The event was postponed because of logistical difficulties.','그 행사는 물류상의 어려움 때문에 연기되었다.','logistical problem/support'),
('set up','설립하다; 설치하다','v','The retailer plans to set up a distribution center in Busan.','그 소매업체는 부산에 물류센터를 설립할 계획이다.','set up a company/system/meeting'),
('bump','증가시키다','v','The promotion helped bump online sales by 12 percent.','그 판촉은 온라인 매출을 12퍼센트 증가시키는 데 도움이 되었다.','bump up sales'),
('publicity','홍보; 대중의 관심','n','The product received considerable publicity after the trade show.','그 제품은 무역 박람회 후 상당한 홍보 효과를 얻었다.','receive/generate publicity'),
('promote','홍보하다; 승진시키다','v','The agency was hired to promote the new service.','그 대행사는 새 서비스를 홍보하기 위해 고용되었다.','promote a product / be promoted to'),
('setback','차질; 좌절','n','The construction delay was a temporary setback.','공사 지연은 일시적인 차질이었다.','suffer/face a setback'),
('accounting process','회계 처리 절차','n','The new software simplifies the accounting process.','새 소프트웨어는 회계 처리 절차를 간소화한다.','streamline an accounting process'),
('financial dispute','금전 분쟁','n','The two firms settled their financial dispute out of court.','두 회사는 금전 분쟁을 법정 밖에서 해결했다.','settle a financial dispute'),
('fare','요금','n','The bus fare will increase slightly next month.','버스 요금은 다음 달에 소폭 인상될 것이다.','airfare / bus fare / fare increase'),
('extinction','멸종','n','The program protects rare plants from extinction.','그 프로그램은 희귀 식물이 멸종되는 것을 막는다.','protect/save A from extinction'),
('involvement','참여; 관여','n','Employee involvement is essential to the project’s success.','직원 참여는 프로젝트 성공에 필수적이다.','involvement in'),
('condominium','공동 주택; 콘도','n','The developer will build a condominium near the station.','그 개발업체는 역 근처에 공동 주택을 지을 것이다.','a condominium complex'),
('committed to','~에 전념하는','adj','The company is committed to reducing waste.','그 회사는 폐기물을 줄이는 데 전념하고 있다.','be committed to + 명사/V-ing'),
('tenant','세입자','n','Each tenant must submit a maintenance request in writing.','각 세입자는 유지보수 요청서를 서면으로 제출해야 한다.','commercial tenant / tenant agreement'),
('carry out','수행하다','v','The research team will carry out a customer survey.','연구팀은 고객 설문조사를 실시할 것이다.','carry out a survey/inspection'),
('thoroughness','철저함','n','The auditor was praised for her thoroughness.','그 감사 담당자는 철저함으로 칭찬받았다.','with thoroughness / attention to detail'),
('proposal','제안서','n','The board approved the expansion proposal.','이사회는 확장 제안서를 승인했다.','submit/approve a proposal'),
('attached','첨부된','adj','Please review the attached invoice before making payment.','결제하기 전에 첨부된 청구서를 검토해 주세요.','attached file/document'),
('ask about','~에 관해 질문하다','v','Several clients called to ask about the warranty.','여러 고객이 보증에 관해 질문하려고 전화했다.','ask about + 명사'),
('determine the cause','원인을 규명하다','v','Technicians are trying to determine the cause of the outage.','기술자들은 정전의 원인을 규명하려고 하고 있다.','determine the cause of'),
('investigate','조사하다','v','The safety officer will investigate the accident.','안전 담당자가 그 사고를 조사할 것이다.','investigate + 목적어 (about 없음)'),
('internal audit','내부 감사','n','An internal audit will be conducted next quarter.','다음 분기에 내부 감사가 실시될 것이다.','conduct an internal audit'),
('work instruction','작업 지침서','n','The updated work instruction is available on the intranet.','갱신된 작업 지침서는 사내망에서 확인할 수 있다.','follow a work instruction'),
('in compliance with','~을 준수하여','prep','The equipment was installed in compliance with safety regulations.','그 장비는 안전 규정을 준수하여 설치되었다.','in compliance with rules/regulations'),
('tentative','잠정적인','adj','A tentative schedule will be announced on Friday.','잠정 일정은 금요일에 발표될 것이다.','tentative schedule/agreement'),
('make a request to','~에게 요청하다','v','Employees may make a request to the facilities manager.','직원들은 시설 관리자에게 요청할 수 있다.','make a request to + 사람'),
('embody','구체화하다; 구현하다','v','The new logo can embody the company’s core values.','새 로고는 회사의 핵심 가치를 구현할 수 있다.','embody values/principles'),
('original','독창적인; 원래의','adj','The designer presented an original concept.','그 디자이너는 독창적인 구상을 제시했다.','original idea/design'),
('board','이사회','n','The board will review the merger proposal tomorrow.','이사회는 내일 합병 제안서를 검토할 것이다.','board member / board of directors'),
('chair','위원장','n','The chair of the committee opened the meeting.','위원회 위원장이 회의를 시작했다.','chair of the committee'),
('committee','위원회','n','The committee reached a unanimous decision.','위원회는 만장일치 결정을 내렸다.','committee member / selection committee'),
('be affiliated with','~와 제휴하다','v','The research center is affiliated with a local university.','그 연구센터는 지역 대학과 제휴하고 있다.','be affiliated with'),
('grant','승인하다; 수여하다','v','The city granted the company a construction permit.','시는 그 회사에 건축 허가를 내주었다.','grant A B / grant permission'),
('deliberation','심의; 숙고','n','The proposal is still under deliberation.','그 제안은 아직 심의 중이다.','under deliberation'),
('debate','토론하다; 논쟁','v','The council will debate the issue next week.','의회는 다음 주에 그 사안을 토론할 것이다.','debate + 목적어'),
('sit down with','~와 마주 앉아 논의하다','v','The manager will sit down with union representatives.','관리자는 노조 대표들과 마주 앉아 논의할 것이다.','sit down with + 사람'),
('broadcast','방송하다','v','The awards ceremony will be broadcast live.','시상식은 생방송될 것이다.','be broadcast live'),
('attract','끌어들이다','v','The discount is intended to attract new customers.','그 할인은 신규 고객을 끌어들이기 위한 것이다.','attract customers/attention'),
('take up the offer','제안을 받아들이다','v','Ms. Park decided to take up the offer.','박 씨는 회사의 제안을 받아들이기로 결정했다.','take up an offer'),
('suspect','추측하다; 의심하다','v','Investigators suspect that the damage occurred overnight.','조사관들은 손상이 밤사이에 발생했다고 추측한다.','suspect that + 절'),
('be organized by','~에 의해 주최되다','v','The seminar was organized by the local chamber of commerce.','그 세미나는 지역 상공회의소가 주최했다.','be organized by'),
('come with','~이 딸려 있다','v','The invitation may come with a detailed map.','초대장에는 상세 지도가 딸려 있을 수 있다.','come with + 구성품'),
('as for','~에 관해서는','prep','As for the venue, the committee has not made a decision.','장소에 관해서는 위원회가 아직 결정하지 않았다.','as for + 명사'),
('entry','출품작; 참가자','n','Each entry must be submitted by May 1.','각 출품작은 5월 1일까지 제출되어야 한다.','contest entry / submit an entry'),
('criteria','기준','n','Applicants must meet all selection criteria.','지원자는 모든 선발 기준을 충족해야 한다.','meet criteria; criterion은 단수'),
('come to mind','생각나다','v','Several possible solutions may come to mind.','가능한 해결책 몇 가지가 생각날 수 있다.','come to mind'),
('entrant','참가자','n','Each entrant will receive a confirmation email.','각 참가자는 확인 이메일을 받을 것이다.','contest entrant'),
('cost estimate','비용 견적','n','The contractor provided a detailed cost estimate.','계약업체는 상세한 비용 견적을 제공했다.','provide a cost estimate'),
('cost-effective','비용 효율적인','adj','The new system is a cost-effective solution.','새 시스템은 비용 효율적인 해결책이다.','cost-effective alternative/solution'),
('complimentary consultation','무료 상담','n','The clinic offers a complimentary consultation.','그 병원은 무료 상담을 제공한다.','complimentary = free of charge'),
('administrative work','행정 업무','n','The assistant handles most administrative work.','그 비서는 대부분의 행정 업무를 처리한다.','perform/handle administrative work'),
('regret','유감으로 여기다','v','We regret to inform you that the event has been canceled.','행사가 취소되었음을 알려 드리게 되어 유감입니다.','regret to inform'),
('organize','준비하다; 조직하다','v','Ms. Lee was asked to organize the annual workshop.','이 씨는 연례 워크숍을 준비해 달라는 요청을 받았다.','organize an event'),
('familiar','익숙한','adj','All staff should be familiar with the emergency procedure.','모든 직원은 비상 절차를 숙지해야 한다.','be familiar with'),
('revision','수정; 개정','n','The latest revision of the plan includes a larger lobby.','계획의 최신 수정본에는 더 큰 로비가 포함되어 있다.','make/review a revision'),
('fairly','꽤; 상당히','adv','The instructions are fairly easy to follow.','그 지침은 따르기가 꽤 쉽다.','fairly + 형용사'),
('depletion','고갈','n','Water depletion is a serious concern in the region.','수자원 고갈은 그 지역의 심각한 우려 사항이다.','resource depletion'),
('flammable','가연성의','adj','Flammable materials must be stored separately.','가연성 물질은 별도로 보관해야 한다.','flammable materials'),
('intermittently','간헐적으로','adv','The network may operate intermittently during maintenance.','유지보수 중에는 네트워크가 간헐적으로 작동할 수 있다.','operate intermittently'),
('predominantly','대부분; 주로','adv','The neighborhood is predominantly residential.','그 지역은 대부분 주거 지역이다.','predominantly + 형용사'),
('fringe benefits','부가 급여; 복리후생','n','The position includes generous fringe benefits.','그 직책에는 후한 복리후생이 포함된다.','salary and fringe benefits'),
('rashly','성급하게','adv','The board should not act rashly.','이사회는 성급하게 행동해서는 안 된다.','act rashly'),
('stagnant','정체된','adj','Sales remained stagnant throughout the quarter.','매출은 분기 내내 정체된 상태였다.','remain stagnant'),
('faction','파벌','n','A small faction opposed the proposed merger.','소규모 파벌이 제안된 합병에 반대했다.','a political faction'),
('make up for','만회하다; 보상하다','v','Higher online sales may make up for the decline in store traffic.','온라인 매출 증가가 매장 방문 감소를 만회할 수 있다.','make up for a loss/shortage'),
('vocation','직업; 천직','n','She considers teaching her vocation.','그녀는 가르치는 일을 자신의 천직으로 여긴다.','choose/pursue a vocation'),
('preferential treatment','우대; 특혜','n','Members receive preferential treatment when booking rooms.','회원은 객실 예약 시 우대를 받는다.','receive preferential treatment'),
('commission','위원회; 수수료','n','The commission approved the new safety standard.','위원회는 새 안전 기준을 승인했다.','government commission / sales commission'),
('resemble','닮다; 비슷하다','v','The new model closely resembles its predecessor.','새 모델은 이전 모델과 매우 비슷하다.','resemble + 목적어 (with 없음)'),
('convene','소집하다','v','The chair will convene an emergency meeting.','위원장은 긴급회의를 소집할 것이다.','convene a meeting'),
('levy','부과하다','v','The city may levy a tax on vacant properties.','시는 빈 부동산에 세금을 부과할 수 있다.','levy a tax/fee on'),
('dispense','분배하다; 제공하다','v','The machine dispenses protective gloves.','그 기계는 보호 장갑을 나누어 준다.','dispense medicine/supplies'),
('insulation','단열재','n','The contractor replaced the damaged insulation.','계약업체는 손상된 단열재를 교체했다.','install/replace insulation'),
('succumb to','~에 굴복하다','v','The small retailer may succumb to financial pressure.','그 소매업체는 재정 압박에 굴복할 수 있다.','succumb to pressure/disease'),
('throw out','버리다','v','Please throw out any outdated brochures.','오래된 안내 책자는 모두 버려 주세요.','throw out = discard'),
('detect','감지하다','v','The device can detect minor gas leaks.','그 장치는 작은 가스 누출도 감지할 수 있다.','detect a problem/leak'),
('inadvertently','무심코; 의도치 않게','adv','The employee inadvertently deleted the file.','그 직원은 실수로 파일을 삭제했다.','inadvertently = unintentionally'),
('envision','구상하다; 상상하다','v','The architect envisioned a flexible workspace.','건축가는 유연한 업무 공간을 구상했다.','envision + 명사/V-ing'),
('constituency','유권자 집단; 지지 기반','n','The representative met with members of her constituency.','그 대표는 자신의 지역 유권자들을 만났다.','serve/represent a constituency'),
('indulge in','~에 탐닉하다','v','Guests can indulge in a variety of desserts.','투숙객은 다양한 디저트를 마음껏 즐길 수 있다.','indulge in + 명사/V-ing'),
('quarantine','격리','n','The imported plants were placed in quarantine.','수입된 식물들은 격리 조치되었다.','place/keep in quarantine'),
('incompetent','무능한','adj','The report found the contractor incompetent.','그 보고서는 해당 계약업체가 무능하다고 판단했다.','find + 목적어 + incompetent'),
('incur','초래하다; 부담하다','v','Late cancellations may incur an additional fee.','늦은 취소에는 추가 요금이 발생할 수 있다.','incur costs/debt/a fee'),
('compose','구성하다; 작곡하다','v','Five regional managers compose the advisory panel.','다섯 명의 지역 관리자가 자문단을 구성한다.','be composed of / compose + 목적어'),
('enlightening','유익한; 깨우침을 주는','adj','The guest speaker gave an enlightening presentation.','초청 연사는 유익한 발표를 했다.','an enlightening talk/experience'),
('steadily','꾸준히','adv','Online orders have increased steadily since January.','온라인 주문은 1월 이후 꾸준히 증가했다.','increase/grow steadily'),
('embark on','시작하다; 착수하다','v','The company will embark on a major renovation.','그 회사는 대규모 보수 공사에 착수할 것이다.','embark on a project/journey'),
('affirmative','긍정적인; 찬성의','adj','The board gave an affirmative response.','이사회는 긍정적인 답변을 했다.','affirmative response/action'),
('quantify','수치화하다','v','The survey aims to quantify customer satisfaction.','그 설문은 고객 만족도를 수치화하는 것을 목표로 한다.','quantify costs/results'),
('iteration','반복; 개선 버전','n','The latest iteration of the software is easier to use.','소프트웨어의 최신 개선 버전은 사용하기가 더 쉽다.','the latest iteration of')]

def choices(i, field, pos=None):
    pool=[x for j,x in enumerate(V) if j!=i and (pos is None or x[2]==pos)]
    if len(pool)<3: pool=[x for j,x in enumerate(V) if j!=i]
    return [V[i][field]]+[pool[(i*3+k)%len(pool)][field] for k in range(3)]

out=[]
for i,(word,meaning,pos,sentence,translation,memory) in enumerate(V):
    # stage 1: meaning recognition
    out.append({'id':f'v{i+1:03d}-1','pairId':f'v{i+1:03d}','stage':1,'category':'사진 단어','label':'단어 1/2',
      'q':f'“{word}”의 뜻으로 가장 알맞은 것은?','choices':choices(i,1),'answer':0,
      'translation':f'{word} = {meaning}','why':f'{word}의 핵심 뜻은 “{meaning}”입니다.',
      'wrong':'나머지는 사진에 함께 나온 다른 단어의 뜻으로, 이 단어와 일치하지 않습니다.','memory':memory,'source':'추가 사진 단어'})
    # stage 2: application in an authentic Part 5 sentence
    app_answer=word[3:] if word.startswith('be ') else word
    q=re.sub(re.escape(app_answer),'______',sentence,count=1,flags=re.I)
    word_choices=choices(i,0,pos); word_choices[0]=app_answer
    out.append({'id':f'v{i+1:03d}-2','pairId':f'v{i+1:03d}','stage':2,'category':'사진 단어','label':'Part 5 2/2',
      'q':q,'choices':word_choices,'answer':0,'translation':translation,
      'why':f'문맥과 문장 구조상 “{word}”가 가장 자연스럽습니다.',
      'wrong':f'다른 선택지는 같은 품사이지만 문맥과 연어가 맞지 않습니다. 완성 표현은 “{memory}”입니다.',
      'memory':memory,'source':'추가 사진 단어'})

# Balance A/B/C/D while preserving each pair's stage order.
for i,q in enumerate(out):
    target=i%4; ans=q['choices'][q['answer']]
    rest=[x for j,x in enumerate(q['choices']) if j!=q['answer']]
    rest.insert(target,ans); q['choices']=rest; q['answer']=target
(ROOT/'vocab_questions.js').write_text('window.VOCAB_QUESTIONS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(json.dumps({'words':len(V),'questions':len(out),'answers':[sum(x['answer']==i for x in out) for i in range(4)]},ensure_ascii=False))
