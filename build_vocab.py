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
('fairly','꽤; 상당히; 공정하게','adv','The instructions are fairly easy to follow.','그 지침은 따르기가 꽤 쉽다.','fairly + 형용사 = 꽤 / treat A fairly = A를 공정하게 대하다'),
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

# 추가 사진(두 번째 묶음)에서 읽은 단어·연어. 기존 목록과 겹치는 항목은 제외했다.
V.extend([
('by then','그때까지','adv','The revised policy will be in effect by then.','개정된 정책은 그때까지 시행될 것이다.','by then = by that time'),
('take place','개최되다; 발생하다','v','The awards ceremony will take place in the main hall.','시상식은 본관에서 개최될 것이다.','take place = be held'),
('mandatory','의무적인','adj','Attendance at the safety workshop is mandatory.','안전 워크숍 참석은 의무이다.','mandatory training/requirement'),
('commitment','약속; 헌신','n','The award recognizes her commitment to customer service.','그 상은 고객 서비스에 대한 그녀의 헌신을 인정한다.','commitment to + 명사/V-ing'),
('arrangement','준비; 합의','n','Travel arrangements should be completed by Friday.','출장 준비는 금요일까지 완료되어야 한다.','make travel arrangements'),
('hygiene','위생','n','The restaurant follows strict hygiene standards.','그 식당은 엄격한 위생 기준을 따른다.','hygiene standards/practices'),
('up to date','최신의','adj','Please keep your contact information up to date.','연락처 정보를 최신 상태로 유지해 주세요.','keep A up to date'),
('informative','유익한','adj','The orientation session was highly informative.','오리엔테이션은 매우 유익했다.','an informative session/report'),
('observe','관찰하다; 준수하다','v','All visitors must observe the safety rules.','모든 방문객은 안전 규칙을 준수해야 한다.','observe rules/regulations'),
('operation','운영; 작업','n','Normal operations will resume on Monday.','정상 운영은 월요일에 재개될 것이다.','business operations'),
('printing press','인쇄기','n','The publisher purchased a new printing press.','그 출판사는 새 인쇄기를 구입했다.','operate a printing press'),
('profit','수익','n','The company reported a substantial profit this quarter.','그 회사는 이번 분기에 상당한 수익을 보고했다.','make/report a profit'),
('since then','그 이후로','adv','The branch opened in May and has expanded rapidly since then.','그 지점은 5월에 문을 열었고 그 이후 빠르게 확장되었다.','현재완료 + since then'),
('expose','노출시키다','v','The report may expose weaknesses in the current system.','그 보고서는 현 시스템의 약점을 드러낼 수 있다.','expose A to B'),
('extricate','구출하다; 벗어나게 하다','v','The consultant helped the firm extricate itself from debt.','컨설턴트는 그 회사가 부채에서 벗어나도록 도왔다.','extricate A from B'),
('commence','시작하다','v','Construction will commence early next month.','공사는 다음 달 초에 시작될 것이다.','commence work/operations'),
('volunteer','자원봉사자','n','Each volunteer will receive a name badge.','각 자원봉사자는 명찰을 받을 것이다.','volunteer work / a volunteer'),
('requisition','요청서; 청구','n','Submit a purchase requisition to the finance department.','구매 요청서를 재무부에 제출하세요.','purchase requisition'),
('milestone','중요한 이정표','n','The company celebrated its one-hundredth store as a major milestone.','그 회사는 100번째 매장을 중요한 이정표로 기념했다.','reach/celebrate a milestone'),
('strike a deal','합의하다','v','The two companies hope to strike a deal by Friday.','두 회사는 금요일까지 합의하기를 바란다.','strike a deal with'),
('convention','회의; 대회','n','The annual sales convention begins tomorrow.','연례 영업 대회는 내일 시작된다.','annual convention'),
('as of today','오늘부로','adv','As of today, the new refund policy is in effect.','오늘부로 새 환불 정책이 시행된다.','as of + 날짜/시점'),
('abide by','준수하다','v','All contractors must abide by the building regulations.','모든 계약업체는 건축 규정을 준수해야 한다.','abide by rules/laws'),
('deliver a speech','연설하다','v','The director will deliver a speech at the ceremony.','이사는 기념식에서 연설할 것이다.','deliver/give a speech'),
('in acceptance of','~을 수락하여','prep','She signed the form in acceptance of the offer.','그녀는 제안을 수락하여 서류에 서명했다.','in acceptance of an offer'),
('in honor of','~을 기념하여','prep','A reception was held in honor of the retiring director.','퇴임 이사를 기념하여 리셉션이 열렸다.','in honor of + 사람/행사'),
('collaborate with','~와 협력하다','v','The design team will collaborate with local artists.','디자인팀은 지역 예술가들과 협력할 것이다.','collaborate with + 사람/기관'),
('implement','시행하다','v','The company will implement the revised policy in July.','회사는 7월에 개정 정책을 시행할 것이다.','implement a policy/system'),
('equip A with B','A에게 B를 갖추게 하다','v','The training will equip employees with practical skills.','그 교육은 직원들에게 실무 기술을 갖추게 할 것이다.','equip A with B'),
('argue with','~와 논쟁하다','v','The supplier argued with the contractor over the cost.','공급업체는 비용 문제로 계약업체와 논쟁했다.','argue with 사람 over 사안'),
('alert','경고하다; 알리다','v','The system will alert users to unusual activity.','시스템은 사용자에게 비정상 활동을 알릴 것이다.','alert A to B'),
('encourage','권장하다','v','Managers encourage employees to share ideas.','관리자들은 직원들이 아이디어를 공유하도록 권장한다.','encourage A to V'),
('evaluate','평가하다','v','The committee will evaluate all proposals.','위원회는 모든 제안서를 평가할 것이다.','evaluate performance/proposals'),
('evaluation','평가','n','A performance evaluation is conducted annually.','업무 평가는 매년 실시된다.','performance evaluation'),
('authorize','승인하다; 권한을 주다','v','Only supervisors may authorize overtime work.','감독자만 초과 근무를 승인할 수 있다.','authorize payment/work'),
('comply with','~을 준수하다','v','All products must comply with safety standards.','모든 제품은 안전 기준을 준수해야 한다.','comply with rules/standards'),
('generate','발생시키다; 산출하다','v','The campaign generated strong interest.','그 캠페인은 큰 관심을 불러일으켰다.','generate revenue/interest'),
('withdraw','철회하다; 인출하다','v','The applicant decided to withdraw the request.','지원자는 요청을 철회하기로 결정했다.','withdraw an application/request'),
('withdrawal','철회; 인출','n','The bank charges a fee for each withdrawal.','은행은 인출 건마다 수수료를 부과한다.','cash withdrawal'),
('referee','중재자; 심판','n','An independent referee reviewed the complaint.','독립적인 중재자가 민원을 검토했다.','independent referee'),
('compromise','타협하다; 타협','v','Both parties agreed to compromise.','양측은 타협하기로 합의했다.','reach a compromise'),
('resume','재개하다','v','Regular service will resume after the inspection.','정기 서비스는 점검 후 재개될 것이다.','resume operations/service'),
('outline','개요를 설명하다','v','The report outlines the company’s expansion plan.','그 보고서는 회사의 확장 계획을 개괄한다.','outline a plan/procedure'),
('terminate','종료하다','v','Either party may terminate the contract.','어느 쪽이든 계약을 종료할 수 있다.','terminate a contract/agreement'),
('convey','전달하다','v','The chart conveys the survey results clearly.','그 도표는 설문 결과를 명확히 전달한다.','convey information/message'),
('interact','상호작용하다','v','Visitors can interact with product specialists.','방문객은 제품 전문가들과 상호작용할 수 있다.','interact with'),
('lure','유혹하다; 끌어들이다','v','The discount may lure customers back to the store.','그 할인은 고객들을 매장으로 다시 끌어들일 수 있다.','lure A to/into'),
('compile','편집하다; 수집하다','v','The analyst compiled the monthly sales figures.','분석가는 월별 매출 수치를 수집했다.','compile data/a report'),
('endorse','승인하다; 지지하다','v','The board endorsed the proposed merger.','이사회는 제안된 합병을 승인했다.','endorse a proposal/candidate'),
('verify','확인하다','v','Please verify the delivery address.','배송 주소를 확인해 주세요.','verify information/identity'),
('verification','확인; 검증','n','Identity verification is required for access.','접근하려면 신원 확인이 필요하다.','identity verification'),
('impose','부과하다','v','The city may impose a fine for late payment.','시는 연체에 대해 벌금을 부과할 수 있다.','impose a fine/tax on'),
('inspection','검사; 점검','n','The elevator is closed for a safety inspection.','그 엘리베이터는 안전 점검 때문에 운행을 중단했다.','conduct/pass an inspection'),
('commemorate','기념하다','v','The event commemorates the company’s anniversary.','그 행사는 회사 창립 기념일을 기념한다.','commemorate an anniversary'),
('acquaint A with B','A에게 B를 숙지시키다','v','The guide acquaints visitors with local customs.','그 안내서는 방문객에게 지역 관습을 숙지시킨다.','acquaint A with B'),
('deliberate','심사숙고하다','v','The panel will deliberate before announcing its decision.','심사단은 결정을 발표하기 전에 숙고할 것이다.','deliberate on/over'),
('acquire','얻다; 인수하다','v','The company plans to acquire a smaller competitor.','그 회사는 더 작은 경쟁사를 인수할 계획이다.','acquire skills/assets/a company'),
('acquisition','인수; 취득','n','The acquisition was completed last month.','그 인수는 지난달 완료되었다.','complete an acquisition'),
('be intended for','~을 위해 만들어지다','v','This manual is intended for new employees.','이 설명서는 신입 직원을 위한 것이다.','be intended for + 대상'),
('surpass','초과하다','v','Quarterly sales surpassed expectations.','분기 매출은 기대치를 넘어섰다.','surpass expectations/a target'),
('excessively','지나치게','adv','The machine should not vibrate excessively.','그 기계는 지나치게 진동해서는 안 된다.','excessively high/expensive'),
('compliant','준수하는','adj','The new equipment is fully compliant with the standard.','새 장비는 그 기준을 완전히 준수한다.','be compliant with'),
('compliance','준수','n','The audit checks compliance with safety rules.','감사는 안전 규정 준수 여부를 확인한다.','compliance with'),
('generation','세대; 발생','n','The product is popular with a younger generation.','그 제품은 젊은 세대에게 인기가 있다.','a new generation of'),
('relieve','완화하다','v','The new procedure will relieve pressure on staff.','새 절차는 직원들의 부담을 덜어 줄 것이다.','relieve pressure/stress'),
('aggravate','악화시키다','v','Further delays could aggravate the problem.','추가 지연은 문제를 악화시킬 수 있다.','aggravate a problem/injury'),
('pursue','추구하다','v','The company will pursue new business opportunities.','그 회사는 새로운 사업 기회를 추구할 것이다.','pursue a goal/career'),
('acquaintance','지인','n','She was referred by a business acquaintance.','그녀는 사업상 지인의 추천을 받았다.','a business acquaintance'),
('deliberately','일부러; 신중하게','adv','The files were deliberately removed.','그 파일들은 의도적으로 삭제되었다.','deliberately = intentionally'),
('entail','수반하다','v','The position entails frequent business travel.','그 직책은 잦은 출장을 수반한다.','entail + 명사/V-ing'),
('appreciate','이해하다; 감사하다','v','We appreciate your prompt response.','신속한 답변에 감사드립니다.','appreciate + 명사/V-ing'),
('remit','송금하다','v','Please remit payment within ten business days.','영업일 기준 10일 이내에 대금을 송금해 주세요.','remit payment'),
('remittance','송금액; 송금','n','The supplier confirmed receipt of the remittance.','공급업체는 송금액 수령을 확인했다.','send/receive a remittance'),
('wire','송금하다','v','The client will wire the deposit tomorrow.','고객은 내일 보증금을 송금할 것이다.','wire money/a deposit'),
('fluctuate','변동하다','v','Fuel prices fluctuate throughout the year.','연료 가격은 연중 변동한다.','prices/rates fluctuate'),
('retrieve','회수하다','v','Users can retrieve archived files online.','사용자는 보관된 파일을 온라인으로 회수할 수 있다.','retrieve data/files'),
('retrieval','검색; 복구','n','The system allows quick data retrieval.','그 시스템은 빠른 데이터 검색을 가능하게 한다.','data retrieval'),
('forcefully','강력하게','adv','The director spoke forcefully in favor of the proposal.','이사는 그 제안에 찬성하며 강력하게 말했다.','argue/speak forcefully')])

# Third photo batch: mixed vocabulary and words with multiple business meanings.
V.extend([
('conduct','수행하다; 행동하다','v','The firm will conduct a customer survey next week.','그 회사는 다음 주 고객 설문조사를 실시할 것이다.','conduct a survey / conduct oneself'),
('carry out','수행하다','v','The laboratory will carry out additional tests.','연구소는 추가 검사를 수행할 것이다.','carry out a task/test'),
('assure A of B','A에게 B를 보장하다','v','We assure clients of complete confidentiality.','우리는 고객에게 완전한 기밀 유지를 보장한다.','assure A of B / assure A that S+V'),
('convince','납득시키다','v','The report convinced investors of the plan’s value.','그 보고서는 투자자들에게 계획의 가치를 납득시켰다.','convince A of B / convince A to V'),
('indicator','지표','n','Sales growth is a useful indicator of demand.','매출 성장은 수요를 보여 주는 유용한 지표다.','an indicator of'),
('indicative','나타내는; 시사하는','adj','The results are indicative of strong demand.','그 결과는 강한 수요를 시사한다.','be indicative of'),
('prevent A from V-ing','A가 V하지 못하게 막다','v','The barrier prevents water from entering the warehouse.','그 장벽은 물이 창고로 들어오는 것을 막는다.','prevent A from V-ing'),
('release','공개하다; 출시하다','v','The company will release its annual report Friday.','회사는 금요일에 연례 보고서를 공개할 것이다.','release a report/product'),
('as indicated','표시된 대로','adv','Submit the form as indicated in the instructions.','안내문에 표시된 대로 양식을 제출하세요.','as indicated below/above'),
('soar','급등하다','v','Online orders soared during the promotion.','판촉 기간에 온라인 주문이 급증했다.','prices/sales soar'),
('plummet','폭락하다','v','Shipping costs plummeted after fuel prices fell.','연료 가격이 하락한 뒤 운송비가 급락했다.','prices/costs plummet'),
('guarantee','보장하다; 보증','v','The warranty guarantees free repairs for one year.','그 보증서는 1년간 무료 수리를 보장한다.','guarantee + 명사 / guarantee that'),
('retain','유지하다; 보유하다','v','The company offers bonuses to retain skilled workers.','회사는 숙련 직원을 유지하기 위해 보너스를 제공한다.','retain staff/control'),
('afford','여유가 있다','v','The department cannot afford further delays.','그 부서는 더 이상의 지연을 감당할 여유가 없다.','can afford to V / afford + 명사'),
('affordable','가격이 알맞은','adj','The hotel offers affordable rooms near the station.','그 호텔은 역 근처에 가격이 알맞은 객실을 제공한다.','affordable price/housing'),
('affordability','가격 부담 가능성','n','The policy improves housing affordability.','그 정책은 주택 가격 부담 가능성을 개선한다.','housing affordability'),
('enlarge','확대하다','v','Click the image to enlarge the floor plan.','평면도를 확대하려면 이미지를 클릭하세요.','enlarge an image'),
('clarify','명확히 하다','v','Please clarify the payment terms in writing.','지급 조건을 서면으로 명확히 해 주세요.','clarify a point/issue'),
('clarification','설명; 해명','n','Contact us if you need clarification.','설명이 필요하면 저희에게 연락하세요.','seek/provide clarification'),
('modify','수정하다','v','The engineer modified the original design.','기술자가 원래 설계를 수정했다.','modify a plan/design'),
('alter','바꾸다','v','The schedule may be altered without notice.','일정은 예고 없이 변경될 수 있다.','alter a schedule'),
('decline','감소하다; 거절하다','v','Demand declined sharply in the second quarter.','수요는 2분기에 급격히 감소했다.','sales decline / decline an invitation'),
('acknowledge receipt of','수령을 확인하다','v','Please acknowledge receipt of this invoice.','이 송장의 수령을 확인해 주세요.','acknowledge receipt of'),
('acknowledge a contribution','공헌을 인정하다','v','The director acknowledged the team’s contribution.','이사는 팀의 공헌을 인정했다.','acknowledge a contribution'),
('various','다양한','adj','The brochure describes various payment options.','그 안내 책자는 다양한 결제 방법을 설명한다.','various + 복수명사'),
('variable','변수; 변하기 쉬운','adj','Delivery times are variable during winter.','겨울에는 배송 시간이 일정하지 않다.','variable costs/conditions'),
('engage in','참여하다; 종사하다','v','Employees may engage in volunteer activities.','직원들은 봉사 활동에 참여할 수 있다.','engage in + 명사/V-ing'),
('engaging','매력적인','adj','The speaker gave an engaging presentation.','연사는 흥미로운 발표를 했다.','an engaging presentation'),
('engagement','약속; 참여; 고용','n','She canceled a prior engagement to attend the meeting.','그녀는 회의 참석을 위해 기존 약속을 취소했다.','prior engagement / employee engagement'),
('preservative','방부제','n','This product contains no artificial preservatives.','이 제품에는 인공 방부제가 들어 있지 않다.','contain a preservative'),
('obstruct','방해하다; 막다','v','Do not obstruct the emergency exit.','비상구를 막지 마세요.','obstruct an exit/view'),
('expect A to V','A가 V할 것으로 기대하다','v','We expect sales to increase next month.','우리는 다음 달 매출이 증가할 것으로 예상한다.','expect A to V'),
('solicit','요청하다; 모집하다','v','The committee solicited feedback from residents.','위원회는 주민들에게 의견을 요청했다.','solicit feedback/bids'),
('solicitation','요청; 권유','n','The agency issued a solicitation for proposals.','그 기관은 제안서 모집 공고를 냈다.','a solicitation for bids'),
('allocate','할당하다','v','The board allocated funds to employee training.','이사회는 직원 교육에 자금을 할당했다.','allocate A to B'),
('foster','촉진하다; 육성하다','v','The program fosters cooperation among departments.','그 프로그램은 부서 간 협력을 촉진한다.','foster growth/cooperation'),
('promote','촉진하다; 홍보하다','v','The campaign promotes the use of public transit.','그 캠페인은 대중교통 이용을 장려한다.','promote growth/a product'),
('alleviate','완화하다','v','Flexible hours may alleviate traffic congestion.','유연 근무 시간은 교통 혼잡을 완화할 수 있다.','alleviate pain/congestion'),
('omit','생략하다','v','Please do not omit your contact information.','연락처 정보를 빠뜨리지 마세요.','omit details/information'),
('maneuver','조종하다; 책략을 쓰다','v','The driver maneuvered the truck into the loading area.','운전자는 트럭을 하역 구역으로 조종했다.','maneuver a vehicle'),
('observation','관찰; 의견','n','The auditor recorded several observations.','감사관은 몇 가지 관찰 의견을 기록했다.','make an observation'),
('continuation','계속; 연장','n','Funding is essential for the continuation of the program.','자금은 프로그램 지속에 필수적이다.','continuation of'),
('restoration','복구; 복원','n','The restoration of service took two hours.','서비스 복구에는 두 시간이 걸렸다.','restoration of service'),
('reservation','예약; 유보','n','Please confirm your hotel reservation.','호텔 예약을 확인해 주세요.','make/confirm a reservation'),
('facade','정면; 외관','n','Workers repaired the building’s facade.','작업자들은 건물 외관을 수리했다.','building facade'),
('be proficient in','~에 능숙하다','adj','Applicants must be proficient in spreadsheet software.','지원자는 스프레드시트 소프트웨어에 능숙해야 한다.','be proficient in'),
('requirement for','~에 대한 요건','n','Experience is a requirement for the position.','경력은 그 직책의 요건이다.','a requirement for'),
('observant','관찰력이 있는','adj','Observant staff noticed the damaged package.','관찰력이 좋은 직원이 손상된 소포를 발견했다.','an observant employee'),
('abstract','추상적인','adj','The proposal remains too abstract to evaluate.','그 제안은 평가하기에 여전히 너무 추상적이다.','an abstract idea'),
('explore','탐구하다; 검토하다','v','The committee will explore alternative locations.','위원회는 대체 장소를 검토할 것이다.','explore options'),
('perspective','관점; 시각','n','The survey provides a customer perspective.','그 설문은 고객 관점을 제공한다.','from a perspective'),
('adjournment','휴회; 연기','n','The chair announced the adjournment of the meeting.','의장은 회의 휴회를 선언했다.','adjournment of a meeting'),
('sensible','합리적인','adj','Reducing unnecessary travel is a sensible decision.','불필요한 출장을 줄이는 것은 합리적인 결정이다.','a sensible decision'),
('put forward','제시하다','v','The consultant put forward a practical solution.','컨설턴트는 실용적인 해결책을 제시했다.','put forward a proposal'),
('distort','왜곡하다','v','Incomplete data may distort the results.','불완전한 자료는 결과를 왜곡할 수 있다.','distort results/facts'),
('impractical','비현실적인','adj','The original deadline proved impractical.','원래 마감일은 비현실적인 것으로 드러났다.','an impractical plan'),
('suppress','억제하다','v','The new filter suppresses background noise.','새 필터는 배경 소음을 억제한다.','suppress noise/information'),
('surge over','~을 넘어서 급증하다','v','Online sales surged over the previous record.','온라인 매출은 이전 기록을 넘어 급증했다.','surge over a level'),
('pertinent clue','관련 단서','n','The inspector found a pertinent clue in the records.','조사관은 기록에서 관련 단서를 찾았다.','pertinent to / a pertinent clue'),
('counteroffer','대안 제안','n','The seller rejected our counteroffer.','판매자는 우리의 수정 제안을 거절했다.','make/reject a counteroffer'),
('redeem a coupon','쿠폰을 사용하다','v','Customers can redeem a coupon online.','고객은 온라인에서 쿠폰을 사용할 수 있다.','redeem a coupon'),
('intuitively','직관적으로','adv','The controls are arranged intuitively.','조작 장치가 직관적으로 배치되어 있다.','work intuitively'),
('inviting','매력적인','adj','The lobby has a warm and inviting atmosphere.','로비에는 따뜻하고 매력적인 분위기가 있다.','an inviting atmosphere'),
('procrastinate','미루다','v','Do not procrastinate when renewing your license.','면허 갱신을 미루지 마세요.','procrastinate on/about'),
('continually','계속해서; 반복적으로','adv','The company continually updates its security system.','회사는 보안 시스템을 계속해서 업데이트한다.','continually improve/update')
])

# Keep one study pair per headword even when it appeared in more than one photo batch.
_seen=set();V=[x for x in V if not (x[0].lower() in _seen or _seen.add(x[0].lower()))]

def choices(i, field, pos=None):
    pool=[x for j,x in enumerate(V) if j!=i and (pos is None or x[2]==pos)]
    if len(pool)<3: pool=[x for j,x in enumerate(V) if j!=i]
    return [V[i][field]]+[pool[(i*3+k)%len(pool)][field] for k in range(3)]

out=[]
SURFACE={
 'equip A with B':'equip','argue with':'argued','acquaint A with B':'acquaints',
 'assure A of B':'assure','prevent A from V-ing':'prevents','modify':'modified',
 'acknowledge a contribution':'acknowledged','expect A to V':'expect','surge over':'surged'
}
MEANING_BY_FORM={}
for _w,_m,*_ in V:
    MEANING_BY_FORM[_w.lower()]=_m
    MEANING_BY_FORM[SURFACE.get(_w,_w[3:] if _w.startswith('be ') else _w).lower()]=_m
for i,(word,meaning,pos,sentence,translation,memory) in enumerate(V):
    # stage 1: meaning recognition
    out.append({'id':f'v{i+1:03d}-1','pairId':f'v{i+1:03d}','stage':1,'category':'사진 단어','label':'단어 1/2',
      'q':f'“{word}”의 뜻으로 가장 알맞은 것은?','choices':choices(i,1),'answer':0,
      'translation':f'{word} = {meaning}','why':f'{word}의 핵심 뜻은 “{meaning}”입니다.',
      'wrong':'나머지는 사진에 함께 나온 다른 단어의 뜻으로, 이 단어와 일치하지 않습니다.','memory':memory,'source':'추가 사진 단어'})
    # stage 2: application in an authentic Part 5 sentence
    app_answer=SURFACE.get(word,word[3:] if word.startswith('be ') else word)
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
    if q['stage']==1:
        reasons=[]
        for j,c in enumerate(q['choices']):
            owners=[w for w,m,*_ in V if m==c]
            owner=' / '.join(owners[:2]) if owners else '다른 사진 단어'
            reasons.append(f'{"ABCD"[j]}. {c}: '+(f'“{V[i//2][0]}”의 핵심 뜻이므로 정답입니다.' if j==q['answer'] else f'이 뜻은 “{owner}”에 해당하므로 오답입니다.'))
        q['wrongReasons']=reasons
    else:
        target_word=V[i//2][0];target_meaning=V[i//2][1]
        reasons=[]
        for j,c in enumerate(q['choices']):
            meaning=MEANING_BY_FORM.get(c.lower(),'사진에 나온 다른 표현')
            if j==q['answer']:
                reasons.append(f'{"ABCD"[j]}. {c}: “{target_meaning}”라는 뜻으로 문맥과 문장 구조를 모두 충족하는 정답입니다.')
            else:
                reasons.append(f'{"ABCD"[j]}. {c}: “{meaning}”라는 뜻입니다. 이 문장에는 “{target_word}({target_meaning})”가 필요하므로 오답입니다.')
        q['wrongReasons']=reasons
(ROOT/'vocab_questions.js').write_text('window.VOCAB_QUESTIONS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(json.dumps({'words':len(V),'questions':len(out),'answers':[sum(x['answer']==i for x in out) for i in range(4)]},ensure_ascii=False))
