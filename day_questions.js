const dayQuestions=[];
const dayNotes={
'ours':['문법·대명사','소유대명사 ours가 ‘우리의 제안’을 대신한다. ours = our proposal. us는 목적격, we는 주격, ourselves는 재귀대명사다.'],
'entirety':['연어','in its entirety는 ‘전체가, 전부’라는 고정 표현이다. 패러프레이징: completely / as a whole.'],
'coordinators':['문법·품사','빈칸은 consent의 주어 자리다. 복수 사람명사 coordinators가 동사원형 consent와 수일치한다.'],
'with':['동사 결합','shop with + 업체는 ‘그 업체에서 구매하다’라는 결합이다. 문맥상 맞춤가구 업체를 이용했다는 뜻이다.'],
'account':['연어','important account는 회사에 중요한 ‘거래처/고객사’를 뜻한다. contract는 계약 자체이므로 rush order의 주체가 될 수 없다.'],
'any':['문법·한정사','명령문에서 불특정한 복수명사 system failures를 받으므로 any가 자연스럽다. every 뒤에는 단수명사가 와야 한다.'],
'immediate':['연어','immediate job openings는 ‘즉시 채용 가능한 공석’이다. immediate opening / immediate vacancy가 TOEIC 빈출 연어다.'],
'inadvertently':['어휘·부사','inadvertently = unintentionally, accidentally(의도치 않게). 동사 omitted를 수식하는 부사 자리다.'],
'protection':['문법·품사','improve 뒤 목적어가 필요하므로 명사 protection이 정답이다. protect는 동사, protector는 사람/도구, protectively는 부사다.'],
'Since':['문법·접속사','Since + 완전한 절은 ‘~이므로’라는 이유를 나타낸다. 패러프레이징: Because / As.'],
'which':['문법·관계대명사','쉼표 뒤 계속적 용법이며 앞의 vouchers를 받아 주어 역할을 하므로 which가 필요하다. that은 계속적 용법에 쓰지 않는다.'],
'occasionally':['문법·품사','writes를 수식하는 빈도부사 자리다. occasionally = from time to time. occasion은 명사, occasional은 형용사다.'],
'various':['문법·형용사','selection을 수식하는 형용사 various가 필요하다. various + 복수명사, a variety of + 복수명사도 함께 외운다.'],
'leveled':['연어','level off = 증가·감소 후 안정되다. 패러프레이징: stabilize / remain steady.'],
'from':['문법·동사 구조','prevent A from -ing는 ‘A가 ~하지 못하게 하다’라는 고정 5형식 구조다.'],
'measure':['연어','measure the effects/impact는 ‘영향을 측정하다’. 패러프레이징: assess / evaluate the effects.'],
'fairly':['문법·부사','형용사 common을 수식하는 정도부사다. fairly common = quite common. evenly는 ‘고르게’라 의미가 다르다.'],
'respectful':['연어','be respectful of + 사람/의견 = ~을 존중하다. respect는 명사·동사, respective는 ‘각각의’다.'],
'representative':['복합명사','sales representative = 영업 담당자. 뒤의 will address의 사람 주어가 필요하다.'],
'received':['연어','be well received = 좋은 반응을 얻다. 패러프레이징: be favorably reviewed / gain a positive response.'],
'otherwise':['연어','unless otherwise specified = 달리 명시되지 않는 한. 계약·안내문에서 매우 자주 나오는 고정 표현이다.'],
'represents':['연어','represent the interests of = ~의 이익을 대변하다. 단수 주어 Council과 represents가 수일치한다.'],
'deeply':['연어','be deeply involved in = ~에 깊이 관여하다. involved를 수식하는 정도부사다.'],
'who':['문법·관계대명사','선행사가 사람 Mr. Martinelli이고 관계절에서 started의 주어이므로 who가 정답이다. whom은 목적격이다.'],
'into':['연어','factor A into B = A를 B에 반영하다. 수동형 be factored into도 함께 외운다.'],
'acquisition':['어휘·연어','acquisition of A by B = B에 의한 A의 인수. merger and acquisition(M&A)과 함께 외운다.'],
'personnel':['수일치·명사','personnel은 직원들을 집합적으로 나타내며 형태 변화 없이 복수 취급한다. laboratory personnel = 연구실 직원.'],
'some':['문법·대명사','some of + 소유격/관사 + 복수명사 구조다. 동사 need도 복수 주어와 일치한다.'],
'contractually':['연어','be contractually obligated to V = 계약상 ~할 의무가 있다. contractually는 obligated를 수식하는 부사다.'],
'determined':['연어','be determined to V = ~하기로 굳게 결심하다. appear determined to V 구조다.'],
'them':['문법·대명사','purchase의 목적어로 앞의 replacement parts를 대신하는 목적격 복수대명사 them이 필요하다.'],
'highly':['연어','be highly recommended = 적극 추천되다. highly + recommended/qualified/effective가 빈출 결합이다.'],
'Attendance':['문법·품사','문장 주어 자리에는 명사 Attendance(참석률/참석)가 필요하다. attend는 동사, attendee는 참석자다.'],
'expansion':['연어','expansion of sales = 판매 확대. thanks to 뒤에는 명사구가 와야 한다.'],
'delivery':['복합명사','delivery date = 배송일. 앞의 명사가 뒤 명사를 수식하는 복합명사다.'],
'closing':['문법·동명사','전치사 by 뒤에는 명사 또는 동명사 -ing가 와야 한다. by closing = 폐쇄함으로써.'],
'creative':['문법·형용사','professional designers를 수식하는 형용사 creative가 필요하다. creatively는 부사다.'],
'Even though':['문법·접속사','Even though + 완전한 절은 ‘비록 ~이지만’이라는 양보. 패러프레이징: Although.'],
'significant':['연어','significant improvement/increase/decrease는 ‘상당한 개선/증가/감소’라는 빈출 연어다.'],
'exciting':['분사 형용사','experience가 사람에게 흥미를 주므로 -ing형 exciting. 사람의 감정은 excited를 쓴다.'],
'nor':['문법·상관구문','not A, nor B = A도 아니고 B도 아니다. 앞의 부정 내용을 이어 추가한다.'],
'asked':['문법·수동태','be asked to V = ~하도록 요청받다. residents가 대피 요청을 받는 수동 관계다.'],
'Strategically':['문법·분사구문','located를 수식하여 ‘전략적으로 위치한’이 되므로 부사 Strategically가 필요하다.'],
'qualified':['연어','be qualified for/to V = ~할 자격이 있다. 여기서는 trained를 수식하는 형용사/분사 qualified.'],
'remains':['문법·2형식','remain + 명사/형용사는 ‘계속 ~이다’. 패러프레이징: continue to be.'],
'advised':['연어','Please be advised that = ~임을 알려드립니다. 공지·이메일의 고정 표현이다.'],
'aware':['연어·문형','be aware that + 절 = ‘~임을 알고 있다/유의하다’. Please be aware that은 제한이나 마감 조건을 알리는 공지의 고정 표현이며 Please note that과 패러프레이징된다.'],
'surrounding':['분사 형용사','surrounding property/area = 주변 부지/지역. 현재분사가 명사를 수식한다.'],
'within':['전치사','within + 범위/문서 = ~안에. final slide within the presentation처럼 전체 안의 위치를 나타낸다.'],
'professionals':['문법·명사','전치사 for 뒤에서 ‘전문가들’을 뜻하는 복수 사람명사가 필요하다.'],
'mandatory':['연어','It is mandatory that S + 동사원형 = S가 ~하는 것은 의무다. 패러프레이징: required / compulsory.'],
'frequently':['문법·빈도부사','offers를 수식하는 빈도부사. frequently = often.'],
'proficient':['연어','be proficient at/in + 명사·-ing = ~에 능숙하다. 패러프레이징: be skilled at.'],
'find':['문법·5형식','find + 목적어 + 형용사 = 목적어가 ~하다고 여기다. consumers find chips appetizing.'],
'all':['문법·수량표현','all of + the/소유격 + 복수명사. every는 of와 직접 결합하지 않고 every member처럼 쓴다.'],
'appraise':['어휘·연어','appraise damage/value = 손해·가치를 평가하다. assess/evaluate와 패러프레이징된다.'],
'reimburse':['연어','reimburse A for B = A에게 B 비용을 변제하다. compensate A for B와 유사하다.'],
'apparently':['문법·부사','형용사 clear를 수식하는 부사 apparently가 필요하다. not entirely/apparently clear 문맥.'],
'whether':['문법·명사절','whether S+V = ~인지 여부. regardless of whether는 고정 연결이다.'],
'responds':['시제·수일치','조건절 If 안에서는 미래 의미라도 현재시제를 쓰며 단수 주어 company에 responds가 일치한다.'],
'will be giving':['시제','정해진 미래 일정에서 미래진행형 will be giving이 자연스럽다. give A a tour = A에게 견학을 제공하다.'],
'Although':['문법·접속사','Although + 절은 양보 관계를 만든다. Even though와 패러프레이징된다.'],
'will be outsourcing':['시제·어휘','미래 시점 Starting in January와 맞는 미래진행형. outsource operations = 업무를 외주화하다.'],
'However':['연결어','앞의 기대와 뒤의 예외가 대조되므로 However. 패러프레이징: Nevertheless / Nonetheless.'],
'in order to':['문법·목적','in order to + 동사원형은 목적 ‘~하기 위해’. 패러프레이징: to / so as to.'],
'they':['문법·삽입절','politicians (whom) they believed to be…에서 they는 believed의 주어다. 목적격 관계대명사가 생략된 구조다.'],
'attend':['문법·타동사','attend는 3형식 타동사라 seminar를 직접 받는다. attend a seminar = participate in a seminar. attend to는 ‘돌보다’다.'],
'performance':['복합명사','sales performance = 판매 실적. perform는 동사, performing은 분사다.'],
'exceptional':['연어','exceptional individuals/candidates = 뛰어난 지원자. 명사를 수식하는 형용사 자리다.'],
'expect':['문법·동사','Although절의 주어 many 뒤에 복수 동사 expect가 필요하다. expectation은 명사다.'],
'provider':['연어','a provider of services = 서비스 제공업체. provide A with B / provide B for A도 함께 외운다.'],
'investigation':['연어','investigation into + 대상 = ~에 대한 조사. 패러프레이징: research into / inquiry into.'],
'financial':['문법·형용사','institutes를 수식하는 형용사 financial이 필요하다. financially는 부사다.'],
'comes':['연어','come with = ~이 딸려 있다/포함되다. 패러프레이징: be equipped with / include.'],
'uncomfortably':['문법·부사','hot을 수식하는 정도부사. uncomfortably hot = 불쾌할 정도로 더운.'],
'for':['전치사 연어','goals for the next fiscal year처럼 대상 기간을 나타낸다.'],
'dedicated':['연어','be dedicated to + 명사/-ing = ~전용이다/헌신하다. channel dedicated to sports.'],
'completely':['문법·부사','finished를 수식하는 부사. complete는 형용사·동사이므로 이 자리에는 맞지 않는다.'],
'before':['전치사·시점','before the due date = 마감일 전에. 패러프레이징: prior to the deadline / ahead of schedule.'],
'finally':['문법·부사','approve를 수식하며 여러 반응 끝의 최종 결정을 나타낸다. lastly는 목록의 마지막 항목에 주로 쓴다.'],
'demand':['연어','an increase in demand = 수요 증가. 패러프레이징: growing demand.'],
'reasonable':['연어','at reasonable prices = 합리적인 가격에. prices를 수식하는 형용사다.'],
'If':['문법·조건절','If + 현재, 주절 will… 구조의 1차 조건문이다. 조건절에서는 미래 의미에도 현재시제를 쓴다.'],
'widely':['연어','be widely recognized/used/available = 널리 인정받다/사용되다/이용 가능하다.'],
'declined':['어휘·타동사','decline an offer = 제안을 정중히 거절하다. 패러프레이징: turn down / reject.'],
'whichever':['문법·복합관계형용사','whichever + 명사 = 어느 것이든. whichever ones you took가 bring back의 목적어다.'],
'Even if':['문법·가정 양보','Even if = 설령 ~하더라도. 사실을 전제하는 even though와 구별한다.'],
'no more than':['수량표현','no more than = 고작/최대 ~. 패러프레이징: at most.'],
'biased':['어휘','biased news = 편향된 뉴스. unbiased/objective news와 반대다.'],
'trait':['연어','personal/character trait = 특성. diligence is an important trait.'],
'elsewhere':['문법·부사','found elsewhere = 다른 곳에서 발견된. where는 선행사나 절 구조가 더 필요하다.'],
'convinced':['연어','be convinced of/about = ~을 확신하다. convince A of B의 수동형이다.'],
'attributed':['연어','attribute A to B / A be attributed to B = A를 B의 결과로 보다. result from과 패러프레이징된다.'],
'institute':['어휘','교육 기관인 ballet institute를 가리킨다. institution과 의미가 유사하다.'],
'delighted':['연어','be delighted to V = 기꺼이/매우 기쁘게 ~하다. pleased/happy to V와 패러프레이징된다.'],
'In addition':['연결어','앞 문장에 경력 정보를 추가하므로 In addition. 패러프레이징: Additionally / Furthermore.'],
'Consequently':['연결어','다양한 연령을 지도한 경험의 결과로 스타일 조정이 가능하므로 Consequently. therefore/as a result와 유사하다.'],
'rate':['어휘·연어','discount rate = 할인율. special rate는 특별 요금이라는 뜻으로 호텔 문맥에 적합하다.'],
'Decorated':['분사구문','(The rooms are) decorated with…가 축약된 과거분사구문. 방이 장식되는 수동 관계다.'],
'They':['대명사','앞의 deluxe rooms를 받는 복수 주격대명사 They가 새 문장의 주어다.'],
'about':['연어','inform A about/of B = A에게 B를 알리다. Thank you for informing us about…'],
'For this reason':['연결어','팀을 파견했다는 원인 뒤에 수거될 것이라는 결과가 오므로 For this reason.'],
'fulfill':['연어','help + 목적어 + (to) 동사원형. fulfill a commitment/obligation = 약속·의무를 이행하다.'],
'compelling':['연어','compelling advertisement/argument = 설득력 있고 눈길을 끄는 광고/주장. persuasive와 유사하다.'],
'specifications':['어휘·복수명사','several 뒤에는 복수 가산명사 specifications. product specifications = 제품 사양.'],
'yet':['상관 표현','difficult yet beneficial = 어렵지만 유익한. yet은 두 형용사를 대조하며 but과 패러프레이징된다.'],
'It has been praised for its sets and costumes.':['패러프레이징·문맥 삽입','공연장이 투어 대상이라는 앞뒤 문맥에 공연의 세트와 의상이 호평받았다는 평가를 덧붙이는 문장이다. be praised for는 ‘~으로 호평받다’이며 receive favorable reviews for와 패러프레이징된다.'],
'All proposals and bids must be received by August 31.':['문맥 삽입·기한 표현','입찰 안내문의 핵심인 제출 마감일을 알려 주는 문장이다. must be received by + 날짜는 ‘그 날짜까지 접수되어야 한다’는 뜻이며 submission deadline과 연결된다.'],
'You can view my dancing videos online.':['문맥 삽입·근거 제시','지원자가 자신의 능력을 확인할 수 있는 자료를 제시하는 흐름이다. view my videos는 앞서 말한 경력·실력을 입증하는 portfolio/sample work의 패러프레이징이다.'],
'The card will not be charged until 24 hours before check-in.':['문맥 삽입·결제 조건','호텔 예약 페이지에서 카드 결제 시점을 구체화하는 문장이다. not A until B는 ‘B가 되어서야 A하다’이므로 체크인 24시간 전까지는 청구되지 않는다는 뜻이다.'],
'Due to the holiday, replacement crews are working this week.':['원인·결과','대체 인력이 근무하는 이유를 직접 설명한다. due to + 명사 = because of + 명사이며, holiday가 원인이고 replacement crews working이 결과다.'],
'Next, we will gather feedback from potential customers.':['글의 순서·연어','제품 개발 절차에서 다음 단계를 알리는 문장이다. gather feedback from customers는 ‘고객 의견을 수집하다’라는 연어이며 conduct customer research와 의미가 통한다.']
};
function dayExplanation(q,c,a,extra){
  if(extra)return extra;
  const ans=c[a],note=dayNotes[ans]||['문맥·구조',`문장의 의미와 구조상 ${ans}가 가장 자연스럽다.`];
  const completed=q.replace('______',`【${ans}】`).replace(/-{3,}/,`【${ans}】`);
  return `<b>정답: ${ans}</b><br><br><b>완성 문장</b><br>${completed}<br><br><b>${note[0]}</b><br>${note[1]}<br><br><b>오답 함정</b><br>${c.filter((_,i)=>i!==a).join(' / ')}는 이 문장의 품사·문장 구조·의미 또는 고정 결합에 맞지 않는다. 정답 단어만 외우지 말고 위의 결합 단위로 암기하세요.`;
}
function D(day,n,q,c,a,e){dayQuestions.push({id:`d${day}-${n}`,day:`DAY ${day}`,tag:`DAY ${day}`,q,c,a,e:dayExplanation(q,c,a,e)})}
// DAY 1 — Word 통합 문제지 1~30
D(1,1,'After a thorough review of all the suggestions, it was clear that ______ was the most realistic proposal.',['us','we','ours','ourselves'],2);
D(1,2,'All exercise equipment in the Ultimate Fitness has been replaced in its ______ with new machines from Loctek Ergonomic.',['entirety','demand','storage','capacity'],0);
D(1,3,'Campus volunteer ______ consent to the partnership with local organizations to expand community service opportunities.',['coordinates','coordination','coordinators','coordinated'],2);
D(1,4,'After searching for hours, Ms. Mackensie finally decided to shop ______ Interior Define for custom furniture that matched her style perfectly.',['for','before','with','into'],2);
D(1,5,'Due to Corner Café being an important ______, we need to handle their rush order with the highest priority.',['contract','promotion','speaker','account'],3);
D(1,6,'When checking the office equipment, please record ______ system failures in the green box on Ms. Ryoko’s desk.',['which','that','every','any'],3);
D(1,7,'At Max Cargo Company, there are several ______ job openings for delivery truck drivers with at least 3 years of industry experience.',['immediate','talented','direct','classic'],0);
D(1,8,'The Nevada Transport Authority’s recent analysis of cities with subway systems ______ omitted Boulder City from its report.',['steadily','inadvertently','sustainably','independently'],1);
D(1,9,'Clio Snacks’ design team has developed new packaging ideas that can improve product ______.',['protects','protection','protector','protectively'],1);
D(1,10,'______ the company’s business calendar is now posted online, paper copies will no longer be distributed.',['Regardless of','Since','In case of','Besides'],1);
D(1,11,'Included in the information packet are three meal vouchers, ______ will allow you to eat at Leticore Hotel’s in-house restaurant.',['where','whose','which','what'],2);
D(1,12,'Rebecca Madison, staff writer at Boston Daily, writes only ______ about fashion, preferring to focus primarily on local news and culture.',['occasion','occasions','occasional','occasionally'],3);
D(1,13,'K.L. Home Deco has a ______ selection of home furnishings in its showroom in Melbourne.',['various','fascinated','limited','largest'],0);
D(1,14,'Stock prices nearly doubled at the first part of the day and then ______ off.',['standardized','downgraded','leveled','commenced'],2);
D(1,15,'A scheduling conflict prevented Mr. Keita ______ attending the investor’s meeting.',['with','from','after','while'],1);
D(1,16,'The purpose of Professor Leonard’s study is to ______ the effects that office lighting has on employee productivity.',['prohibit','measure','accomplish','influence'],1);
D(1,17,'It is ______ common for new restaurants to fail to develop a menu to attract customers at first.',['reasonably','fairly','evenly','occasionally'],1);
D(1,18,'You should be ______ of other people’s points of view during staff meetings.',['respect','respective','respectful','respected'],2);
D(1,19,'A sales ______ from Vallejo Beverages will address student interns participating in the winter internship program.',['agreement','conference','projection','representative'],3);
D(1,20,'The recently released movie Days of Glory has been well ______ in Korea and the United States.',['opposed','creative','positive','received'],3);
D(1,21,'Utility costs such as water, electricity, and gas are included in the rental price unless ______ specified in the rental agreement.',['once','sooner','otherwise','eventually'],2);
D(1,22,'The Global Glass Manufacturers Council ______ the interests of glass manufacturers around the world.',['represents','reproduces','contributes','operates'],0);
D(1,23,'Mr. Himura has been ______ involved in the development of Visetrix wireless headsets.',['commonly','occasionally','deeply','fondly'],2);
D(1,24,'Mr. Martinelli, ______ started as a stock clerk and is now vice president of marketing, will retire in May.',['who','that','whom','himself'],0);
D(1,25,'The cost of additional exterior paint has been factored ______ the revised estimate.',['into','out','with','upon'],0);
D(1,26,'The letter regarding the proposed ______ of Marcie Law Office by Kapoor Legal Services has arrived.',['acquisition','detachment','document','compliance'],0);
D(1,27,'All laboratory ______ must annually complete a course in safety practices.',['researcher','network','test','personnel'],3);
D(1,28,'Due to unusually high demand, ______ of our lawn supplies need to be restocked.',['some','something','other','each other'],0);
D(1,29,'For three years, you are ______ obligated to pay a 10% commission fee to Aloz Financial every two months.',['responsibly','considerably','contractually','confidently'],2);
D(1,30,'Mr. Karl appears ______ to take on more duties and to have more control over important decisions.',['capable','determined','likable','ambitious'],1);
// DAY 2 — 101~138
D(2,101,'As Kamon Machines discontinued producing replacement parts for old fax machine models, we cannot purchase ______ anymore.',['they','them','their','theirs'],1);
D(2,102,'Mr. Jones has been ______ recommended by most of his former employers.',['high','higher','highest','highly'],3);
D(2,103,'______ at the city festival was significantly lower because the date of the parade was changed with little advance notice.',['Attend','Attendance','Attendees','Attendants'],1);
D(2,104,'Tang Toys increased its second-quarter revenue thanks to the continued ______ of sales in Japan and America.',['assets','expansion','decline','compensation'],1);
D(2,105,'The shipping manager is worried about making the ______ date because of the record snowfall yesterday.',['deliver','delivers','delivery','delivered'],2);
D(2,106,'Komi Motors has overcome the global economic crisis by ______ its manufacturing plant in Eastern Europe.',['close','closing','closed','closes'],1);
D(2,107,'The Fashion Academy has produced ______ professional designers for the competitive fashion industry.',['create','creation','creative','creatively'],2);
D(2,108,'______ it was snowing heavily, many people decided to walk to work to avoid traffic in town.',['Besides','Instead of','Apart from','Even though'],3);
D(2,109,'According to the yearly sales report, the Genelec Factory’s revenue showed ______ improvement after restructuring.',['wealthy','significant','comparing','worsening'],1);
D(2,110,'In the early 20th century, it was quite an ______ experience to travel about 50 miles due to inadequate transportation infrastructure.',['excite','exciting','excited','excitedly'],1);
D(2,111,'Smoking is not allowed inside the petroleum storage area, ______ is it allowed near the petrochemical plant.',['unless','whether','nor','besides'],2);
D(2,112,'All the residents without exception are ______ to evacuate the building during a fire drill.',['spoken','described','asked','realized'],2);
D(2,113,'______ located in the business district, the duty-free shops will open their doors to international tourists.',['Strategy','Strategize','Strategic','Strategically'],3);
D(2,114,'Even though Jason Heavy Industries received many applications, few individuals were ______ trained.',['qualify','qualifies','qualified','qualifications'],2);
D(2,115,'From casinos and shows to fine dining, Las Vegas ______ a world-class vacation destination.',['remains','stays','locates','appears'],0);
D(2,116,'Please be ______ that international bank processing times vary depending on the local banking system.',['advise','advised','advisable','advisory'],1);
D(2,117,'The old industrial park and the ______ property have been redeveloped into a new apartment complex.',['surround','surrounds','surrounded','surrounding'],3);
D(2,118,'Please list the results of Mr. Watson’s research on the final slide ______ the marketing presentation.',['within','of','through','except'],0);
D(2,119,'Most people think art is for the highly gifted or for ______.',['profession','professional','professionals','professionally'],2);
D(2,120,'To prevent workplace accidents, it is ______ that all employees take part in annual safety training.',['ambiguous','mandatory','preventive','appreciative'],1);
D(2,121,'At regular marketing meetings, Mr. Thompson ______ offers innovative strategies.',['frequently','enormously','considerably','promptly'],0);
D(2,122,'______ she quit her job last week, Ms. Parker has time to take a management course.',['Since','When','Despite','Therefore'],0);
D(2,123,'Once employees complete the training, they will be ______ at doing their accounting work.',['flexible','aware','proficient','economical'],2);
D(2,124,'Our survey indicated that most consumers ______ mint-flavored chocolate chips very appetizing.',['take','find','expect','feel'],1);
D(2,125,'According to the revised regulations, ______ of the member nations must undergo periodic audits.',['all','another','every','few'],0);
D(2,126,'The insurance company attempted to ______ the fire damage as accurately as it could.',['avoid','cover','appraise','claim'],2);
D(2,127,'If your bag is not found within 21 days, we will ______ you for any transportation fee.',['provide','reimburse','transfer','allocate'],1);
D(2,128,'Some reasons for the decrease in housing sales are not ______ clear.',['apparently','usually','meticulously','immediately'],0);
D(2,129,'Regardless of ______ an applicant is offered a loan, all applications must be kept for a year.',['whereas','even though','instead','whether'],3);
D(2,130,'If the company ______ to our demands reasonably, the union will resume negotiations.',['respond','responds','will respond','was responding'],1);
D(2,131,'John Baker, a renowned performance director, ______ us a guided tour next Saturday.',['giving','will be giving','was given','give'],1);
D(2,132,'Which sentence best fits the Warren Hall tour memorandum?',['All employees are advised to attend.','A small amount was spent on donations.','It has been praised for its sets and costumes.','Many films will be shown there.'],2);
D(2,133,'______ there is no charge for the tour, every employee must reserve a spot.',['Even if','Since','When','Although'],3);
D(2,134,'Please be ______ that tickets are limited and sign-up ends June 30.',['reluctant','possible','willing','aware'],3);
D(2,135,'Starting in January, Taylor & Murphy Accounting ______ all computer maintenance and data management operations.',['will be outsourcing','outsourced','have been outsourced','outsourcing'],0);
D(2,136,'We expect partner employees on site. ______, we understand that this may not always be possible.',['While','Even','Furthermore','However'],3);
D(2,137,'Extra work will be needed at the start ______ upgrade copper-based networks to fiber optics.',['so that','in order to','which','in case'],1);
D(2,138,'Which sentence best completes the accounting company’s bid letter?',['All proposals and bids must be received by August 31.','Many bidders will compete for the contract.','Paperwork accuracy is important.','Our personnel can improve your efficiency.'],0);
// DAY 3 — 101~146
D(3,101,'The residents supported several politicians ______ believed to be the most honest and prudent.',['they','their','their own','theirs'],0);
D(3,102,'Whoever is willing to ______ today’s informational seminar may do so.',['detect','achieve','attend','notify'],2);
D(3,103,'The company’s best sales ______ was attributable to Mr. Yamada’s team.',['performed','preforms','performing','performance'],3);
D(3,104,'The Empire Hotel is accepting applications from ______ individuals.',['angular','aligned','exceptional','farther'],2);
D(3,105,'Although many ______ a profitable holiday season, the company is concerned about labor costs.',['expect','expectation','are expected','expectantly'],0);
D(3,106,'Night-shift representatives are available ______ 6:00 P.M. to 2:00 A.M.',['between','from','since','beyond'],1);
D(3,107,'Liam Body Care has been a major ______ of massage services for almost 20 years.',['provide','provision','provider','provided'],2);
D(3,108,'Engineers will publicize the results of the ______ into alternative energy.',['understanding','determination','investigation','specification'],2);
D(3,109,'Most of the ______ institutes in Korea are struggling because of online banks.',['financial','financing','finances','financially'],0);
D(3,110,'______ passengers vary in their seat preferences, they can choose seats online.',['Whether','Soon','Why','Since'],3);
D(3,111,'The LCG’s new monitor ______ with a surround-sound speaker and a display stand.',['comes','will come','is come','was coming'],0);
D(3,112,'Only 5 participants finished because it was ______ hot.',['importantly','almost','closely','uncomfortably'],3);
D(3,113,'The board had a strategy meeting on its goals ______ the next fiscal year.',['under','for','alongside','as'],1);
D(3,114,'Albright Media Cable will start a channel ______ to sports and entertainment news.',['permitted','introduced','reported','dedicated'],3);
D(3,115,'Ms. Sutherland finished her work ______ several days before the deadline.',['completely','completed','complete','completing'],0);
D(3,116,'The estimate will be sent ______ the due date.',['along','within','through','before'],3);
D(3,117,'Faced with residents’ reactions, the mayor will ______ approve the proposal.',['lately','finally','infinitely','lastly'],1);
D(3,118,'Due to an increase in ______, customers should expect shipment delays.',['seniority','arrival','demand','certificate'],2);
D(3,119,'Yoon’s Catering offers food items at ______ prices.',['reason','reasonable','reasonably','reasons'],1);
D(3,120,'______ several workers are hired, meeting the construction schedule will not be a problem.',['Except for','Since','Instead of','If'],3);
D(3,121,'The mayor’s contribution was ______ recognized and appreciated.',['widely','wide','wideness','widening'],0);
D(3,122,'Ms. Ayasha kindly ______ a job offer that did not meet her salary expectations.',['prevented','removed','declined','obtained'],2);
D(3,123,'Most staplers are missing, so please bring back ______ ones you took.',['what','whichever','whom','whose'],1);
D(3,124,'______ our CEO does not return next week, meeting rooms will be reserved.',['Although','Even if','Nearly','Despite that'],1);
D(3,125,'Our manager will be available for ______ one hour due to a meeting.',['no more than','hardly any','as soon as','that much'],0);
D(3,126,'The president cautioned that ______ news about him was everywhere and untrue.',['overall','biased','lucrative','modest'],1);
D(3,127,'The most important ______ job candidates must have is diligence.',['act','type','trait','fact'],2);
D(3,128,'Technicians concluded the network problems were the same as those found ______.',['elsewhere','within','otherwise','where'],0);
D(3,129,'All board members are ______ of the success of the organic pet treats.',['convinced','convincing','have convinced','will be convinced'],0);
D(3,130,'The jump in oil prices can be ______ to political uncertainty.',['removed','established','attributed','enlarged'],2);
D(3,131,'Heather has a great deal of respect for the ballet school’s ______.',['exhibition','institute','theater','store'],1);
D(3,132,'She would be ______ to contribute as a dance instructor.',['delighting','delight','delights','delighted'],3);
D(3,133,'She has worked with dancers of many ages. ______, she can adjust her teaching style.',['Otherwise','In addition','Consequently','However'],2);
D(3,134,'Which sentence best completes Heather’s application e-mail?',['I can teach injury prevention.','Download the app to join a class.','I learned from your class.','You can view my dancing videos online.'],3);
D(3,135,'The hotel’s special 30% discount ______ is available throughout March.',['tour','performance','edition','rate'],3);
D(3,136,'______ with calming colors, the deluxe rooms are perfect for relaxing.',['Decorating','To decorate','They decorated','Decorated'],3);
D(3,137,'______ come with a king-sized bed, kitchenette, and spacious bathroom.',['They','Either','Whichever','Fewer'],0);
D(3,138,'Which sentence best completes the hotel Web page?',['A breakfast buffet is served daily.','The card will not be charged until 24 hours before check-in.','Staff will accommodate this request.','Many downtown hotels have vacancies.'],1);
D(3,139,'Thank you for informing us ______ the missed recycling collection.',['with','until','about','into'],2);
D(3,140,'We dispatched a short-notice pickup team. ______, your recycling will be collected by 4 P.M.',['For instance','On the other hand','Apart from that','For this reason'],3);
D(3,141,'Which sentence best explains why replacement crews are working?',['We cannot take unclean items.','Leave feedback on the city site.','A schedule is attached.','Due to the holiday, replacement crews are working this week.'],3);
D(3,142,'Your feedback helps us to ______ our service commitment.',['fulfillment','fulfill','fulfilling','fulfilled'],1);
D(3,143,'Consumers found the handbag ad campaign less ______ than expected.',['gradual','compelling','repetitive','doubtful'],1);
D(3,144,'The design team will receive several ______ outlined by the research team.',['specifying','specification','specifications','specifies'],2);
D(3,145,'Which sentence best completes the handbag development memo?',['Less expensive materials are available.','The commercial features employees.','Next, we will gather feedback from potential customers.','Your efforts made a difference.'],2);
D(3,146,'The additional work will be difficult ______ beneficial.',['for','as','yet','if'],2);
