import json,pathlib
R=pathlib.Path(__file__).parent
# phrase, meaning, sentence with blank, Korean translation, three deliberate traps
C=[
('reach an agreement','합의에 도달하다','After several negotiations, both parties finally ______.','여러 차례 협상 끝에 양측은 마침내 합의에 도달했다.',['arrived an agreement','made to an agreement','reached to an agreement']),
('make a speech','연설하다','The director will ______ at the awards ceremony.','이사는 시상식에서 연설할 것이다.',['do a speech','say a speech','reach a speech']),
('raise questions','의문을 제기하다','The unexplained expense reports may ______ about the project.','설명되지 않은 경비 보고서는 그 사업에 대한 의문을 제기할 수 있다.',['rise questions','lift questions','make up questions']),
('under construction','공사 중인','The east wing is currently ______.','동관은 현재 공사 중이다.',['in construction','at construction','under constructing']),
('by chance','우연히','I found the missing invoice ______.','나는 우연히 분실된 송장을 찾았다.',['by opportunity','in chance','at random chance']),
('by design','고의로; 계획적으로','The two entrances were placed far apart ______.','두 출입구는 계획적으로 멀리 떨어져 배치되었다.',['in design','by designing','at design']),
('strike a deal','거래를 성사시키다','The supplier hopes to ______ with the retailer.','공급업체는 그 소매업체와 거래를 성사시키기를 바란다.',['hit a deal','reach a business','make agreement']),
('take place','개최되다; 일어나다','The annual conference will ______ in Busan.','연례 회의는 부산에서 개최될 것이다.',['take part','make place','occur place']),
('obtain authorization','허가를 받다','Employees must ______ before accessing the records.','직원들은 기록에 접근하기 전에 허가를 받아야 한다.',['make authorization','reach permission','take authorize']),
('acknowledge receipt','수령을 확인하다','Please ______ of the attached contract.','첨부된 계약서를 받았는지 확인해 주세요.',['recognize receipt','acknowledge receiving to','confirming receipt']),
('comply with regulations','규정을 준수하다','All contractors must ______.','모든 계약업체는 규정을 준수해야 한다.',['comply regulations','comply to regulations','follow with regulations']),
('meet the requirements','요건을 충족하다','Only applicants who ______ will be interviewed.','요건을 충족하는 지원자만 면접을 보게 된다.',['reach the requirements','satisfy to requirements','meet with requirements']),
('make a reservation','예약하다','Guests should ______ at least two days in advance.','투숙객은 적어도 이틀 전에 예약해야 한다.',['do a reservation','take a reservation','reserve a reservation']),
('make a decision','결정을 내리다','The board will ______ after reviewing the report.','이사회는 보고서를 검토한 뒤 결정을 내릴 것이다.',['do a decision','reach a decision to','decide a decision']),
('make a bid','입찰하다','Three firms plan to ______ on the construction project.','세 회사가 그 건설 사업에 입찰할 계획이다.',['do a bid','raise a bid on','bid a make']),
('make an effort','노력하다','We must ______ to reduce delivery times.','우리는 배송 시간을 줄이기 위해 노력해야 한다.',['do an effort','take an effort','raise an effort']),
('prolong the life','수명을 연장하다','Regular maintenance can ______ of the equipment.','정기적인 정비는 장비의 수명을 연장할 수 있다.',['lengthen to the life','extend life to','raise the living']),
('adversely affect','불리하게 영향을 미치다','Frequent delays may ______ customer satisfaction.','잦은 지연은 고객 만족도에 악영향을 줄 수 있다.',['adverse affect','affect adversely to','badly effect']),
('undergo renovations','보수 공사를 받다','The lobby will ______ next month.','로비는 다음 달 보수 공사를 받을 것이다.',['receive renovating','undergo renovating to','take renovations of']),
('undergo safety checks','안전 점검을 받다','All vehicles must ______ regularly.','모든 차량은 정기적으로 안전 점검을 받아야 한다.',['take safety checking','undergo safety checking to','receive to checks']),
('supply A with B','A에게 B를 공급하다','The vendor will ______ the necessary parts.','판매업체는 우리에게 필요한 부품을 공급할 것이다.',['supply to us with','supply us to','provide with us']),
('compile sales data','매출 자료를 취합하다','The analyst will ______ from all branches.','분석가는 모든 지점의 매출 자료를 취합할 것이다.',['compose sales data','collect up sales datum','compile with sales data']),
('apply for a position','직책에 지원하다','Qualified candidates may ______ online.','자격을 갖춘 지원자는 온라인으로 그 직책에 지원할 수 있다.',['apply to a position','apply a position','apply with a position']),
('apply to all employees','모든 직원에게 적용되다','The revised policy will ______.','개정된 정책은 모든 직원에게 적용될 것이다.',['apply for all employees','apply all employees','be applied for all employees']),
('approve a request','요청을 승인하다','The manager must ______ before Friday.','관리자는 금요일 전에 그 요청을 승인해야 한다.',['approve of a request','approve to a request','approval a request']),
('approve of a decision','결정에 찬성하다','Most board members ______.','대부분의 이사회 구성원은 그 결정에 찬성한다.',['approve a decision of','approve to a decision','approval of a decision']),
('look over a draft','초안을 검토하다','Please ______ before the meeting.','회의 전에 초안을 검토해 주세요.',['look a draft over to','see over a draft','look on a draft']),
('commit to improving','개선에 전념하다','The company has ______ workplace safety.','회사는 작업장 안전 개선에 전념해 왔다.',['committed to improve','committed improving','committed for improving']),
('lead to higher costs','더 높은 비용으로 이어지다','Poor planning can ______.','부실한 계획은 더 높은 비용으로 이어질 수 있다.',['lead higher costs','result from higher costs','cause to higher costs']),
('participate in a survey','설문조사에 참여하다','More than 500 customers agreed to ______.','500명이 넘는 고객이 설문조사에 참여하기로 했다.',['participate a survey','participate to a survey','attend in a survey']),
('attribute A to B','A를 B 덕분이라고 여기다','The team ______ careful planning.','팀은 성공을 세심한 계획 덕분이라고 여긴다.',['attributes careful planning to its success','attributes its success for careful planning','contributes its success to careful planning']),
('be subject to change','변경될 수 있다','The schedule may ______ without notice.','일정은 예고 없이 변경될 수 있다.',['be subjected for change','be subject of changing','subject to change']),
('face difficulties','어려움에 직면하다','Small businesses often ______ during expansion.','중소기업은 확장 과정에서 종종 어려움에 직면한다.',['meet difficulties with','face with difficulties','encounter to difficulties']),
('invest in real estate','부동산에 투자하다','The fund plans to ______ next year.','그 펀드는 내년에 부동산에 투자할 계획이다.',['invest real estate','invest on real estate','make investment real estate']),
('take responsibility','책임을 지다','The contractor agreed to ______ for the delay.','계약업체는 지연에 대한 책임을 지기로 했다.',['make responsibility','hold responsibility to','take a responsibility for']),
('deliver a presentation','발표하다','Ms. Park will ______ on the new product line.','박 씨는 신제품군에 관해 발표할 것이다.',['make presentation to','say a presentation','present a delivery']),
('file a complaint','불만을 정식으로 제기하다','Customers may ______ through the website.','고객은 웹사이트를 통해 정식으로 불만을 제기할 수 있다.',['make complaint to','submit complaint of','raise a complain']),
('draw attention','관심을 끌다','The unusual display is designed to ______.','그 독특한 진열은 관심을 끌도록 설계되었다.',['pull attention','make attention','attract to attention']),
('boost sales','매출을 증대하다','The promotion is expected to ______.','그 판촉 행사는 매출을 높일 것으로 예상된다.',['raise up sales','increase to sales','boosting sales']),
('ease congestion','혼잡을 완화하다','Flexible work hours could ______ downtown.','유연 근무 시간은 도심 혼잡을 완화할 수 있다.',['easy congestion','relieve from congestion','reduce to congestion'])]
SURFACE={'reach an agreement':'reached an agreement','supply A with B':'supply us with','commit to improving':'committed to improving','attribute A to B':'attributes its success to'}
out=[]
for i,(phrase,meaning,sentence,translation,traps) in enumerate(C):
 meanings=[meaning]+[C[(i+j+1)%len(C)][1] for j in range(3)];surface=SURFACE.get(phrase,phrase)
 qs=[dict(id=f'c{i+1:03d}-1',pairId=f'c{i+1:03d}',stage=1,category='콜로케이션',label='연어 1/2',q=f'“{phrase}”의 뜻으로 가장 알맞은 것은?',choices=meanings,answer=0,translation=f'{phrase} = {meaning}',why=f'“{phrase}”는 “{meaning}”라는 뜻의 고정 결합입니다.',wrong='각 선택지는 다른 콜로케이션의 뜻입니다.',memory=phrase,source='사용자 사진·지정 콜로케이션 형식'),dict(id=f'c{i+1:03d}-2',pairId=f'c{i+1:03d}',stage=2,category='콜로케이션',label='Part 5 2/2',q=sentence,choices=[phrase]+traps,answer=0,translation=translation,why=f'문맥상 자연스러운 고정 결합은 “{phrase}”입니다.',wrong='다른 선택지는 동사와 명사의 결합 또는 전치사 구조가 자연스럽지 않습니다.',memory=phrase,source='사용자 사진·지정 콜로케이션 형식')]
 qs[1]['choices']=[surface]+traps
 for q in qs:
  target=len(out)%4;ans=q['choices'][0];rest=q['choices'][1:];rest.insert(target,ans);q['choices']=rest;q['answer']=target
  q['wrongReasons']=[f'{"ABCD"[j]}. {x}: '+('정답인 고정 결합입니다.' if j==target else '이 문맥에서 쓰는 표준 콜로케이션이 아닙니다.') for j,x in enumerate(q['choices'])]
  out.append(q)
(R/'collocation_questions.js').write_text('window.COLLOCATION_QUESTIONS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print({'collocations':len(C),'questions':len(out)})
