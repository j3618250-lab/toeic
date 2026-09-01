import json, re
from pathlib import Path

ROOT = Path(__file__).parent

items = []

def add(cat, label, q, choices, answer, ko, why, wrong, memory, source="기존 문제은행"):
    items.append({"category":cat,"label":label,"q":q,"choices":choices,"answer":answer,
                  "translation":ko,"why":why,"wrong":wrong,"memory":memory,"source":source})

# 오전 사진 28~38쪽: 각 표의 개별 항목을 최소 한 번씩 출제한다.
gerund_verbs = [
('enjoy','즐기다'),('suggest','제안하다'),('avoid','피하다'),('deny','부인하다'),('resume','재개하다'),
('keep','계속하다'),('give up','포기하다'),('mind','꺼리다'),('finish','끝내다'),('consider','고려하다'),
('recommend','추천하다'),('admit','인정하다'),('discontinue','중단하다'),('quit','그만두다'),
('include','포함하다'),('object to','반대하다'),('postpone','미루다'),('imagine','상상하다')]
subjects=['The employees','Our supervisors','The committee members','The operations managers','The clients']
actions=[
('launching the campaign','to launch the campaign','launched the campaign','launch the campaign','캠페인을 시작하는'),
('revising the schedule','to revise the schedule','revised the schedule','revise the schedule','일정을 수정하는'),
('using the new system','to use the new system','used the new system','use the new system','새 시스템을 사용하는'),
('moving the deadline','to move the deadline','moved the deadline','move the deadline','마감일을 옮기는'),
('opening a new branch','to open a new branch','opened a new branch','open a new branch','새 지점을 여는')]
for i,(v,meaning) in enumerate(gerund_verbs):
    s,forms=subjects[i%len(subjects)],actions[i%len(actions)]; a,to_a,past_a,base_a,ko_a=forms
    prep='' if v!='object to' else ''
    add('동명사 vs to부정사','V-ing vs to V',f'{s} {v} ______.',[a,to_a,past_a,base_a],0,
        f'해당 주체는 {ko_a} 것을 {meaning}.',f'{v}는 목적어로 동명사(V-ing)를 취합니다.',
        'to부정사·과거분사·동사원형은 이 동사의 목적어 형태가 될 수 없습니다.',f'{v} + V-ing = ~하는 것을 {meaning}', '오전 사진 30쪽')

noun_to = [('time','시간'),('right','권리'),('need','필요'),('failure','실패'),('attempt','시도'),('proposal','제안'),('obligation','의무'),('duty','의무'),('way','방법'),('plan','계획'),('intention','의도'),('decision','결정'),('effort','노력'),('opportunity','기회'),('chance','기회'),('ability','능력'),('capacity','능력')]
for i,(n,k) in enumerate(noun_to):
    add('동명사 vs to부정사','명사 + to V',f'The company has the {n} ______ its service.', ['to improve','improving','improved','improves'],0,
        f'그 회사에는 서비스를 개선할 {k}(이)가 있다.',f'{n} 뒤의 to부정사가 명사를 뒤에서 수식합니다.',
        '동명사·분사·동사는 명사의 구체적 내용이나 용도를 나타내는 이 자리에 맞지 않습니다.',f'{n} + to V를 한 덩어리로 암기', '오전 사진 28쪽')

to_patterns=[('be able to','~할 수 있다'),('be anxious to','~하기를 원하다'),('be willing to','기꺼이 ~하다'),('be liable to','~할 것 같다'),('be available to','~할 시간이 있다'),('be pleased to','기쁘게 ~하다'),('be delighted to','기쁘게 ~하다'),('be eager to','~하기를 갈망하다'),('be likely to','~할 것 같다'),('be apt to','~하기 쉽다'),('be about to','막 ~하려고 하다'),('be supposed to','~하기로 되어 있다'),('be intended to','~하도록 의도되다'),('be reluctant to','~하기를 꺼리다'),('be due to','~할 예정이다'),('be scheduled to','~할 예정이다'),('be designed to','~하도록 제작되다'),('be ready to','~할 준비가 되다'),('be invited to','~하라고 초대받다'),('be requested to','~하라고 요청받다'),('be required to','~해야 한다'),('be advised to','~하라고 권고받다'),('be instructed to','~하라고 지시받다')]
for i,(p,k) in enumerate(to_patterns):
    base=p[:-2].strip()
    if base.startswith('be '): base=base[3:]
    add('동명사 vs to부정사','V-ing vs to V',f'The employee is {base.strip()} ______ the orientation.', ['to attend','attending','attended','attend'],0,
        f'그 직원은 오리엔테이션에 참석하도록 되어 있다/참석할 준비가 되어 있다.',f'{p}처럼 이 표현 뒤에는 to부정사가 옵니다.',
        '동명사·과거분사·원형은 이 고정 표현을 완성하지 못합니다.',f'{p} V = {k}', '오전 사진 28~29쪽')

ing_phrases=[('before','~하기 전에'),('after','~한 후에'),('by','~함으로써'),('without','~하지 않고'),('feel like','~하고 싶다'),('be capable of','~할 수 있다'),('have difficulty in','~하는 데 어려움을 겪다'),('look forward to','~을 학수고대하다'),('be committed to','~에 헌신하다'),('be dedicated to','~에 헌신하다'),('upon','~하자마자'),('instead of','~대신에'),('spend time','~하는 데 시간을 쓰다'),('cannot help','~하지 않을 수 없다'),('be busy','~하느라 바쁘다'),('be accustomed to','~에 익숙하다'),('when it comes to','~에 관한 한')]
for i,(p,k) in enumerate(ing_phrases):
    add('동명사 vs to부정사','전치사 + V-ing',f'The staff used the checklist {p} ______ the equipment.', ['inspecting','to inspect','inspected','inspect'],0,
        f'직원들은 장비를 점검하는 것과 관련해 체크리스트를 사용했다.',f'{p} 뒤에는 명사 역할의 동명사 inspecting이 옵니다.',
        'to부정사·과거분사·원형은 전치사 뒤의 명사 자리를 채울 수 없습니다.',f'{p} + V-ing = {k}', '오전 사진 31쪽')

time_place=[('in March','3월에'),('in 2060','2060년에'),('in the summer','여름에'),('in the evening','저녁에'),('in the lobby','로비에서'),('in the waiting room','대기실에서'),('in the lounge','라운지에서'),('at 7 o’clock','7시에'),('at the end of the month','이달 말에'),('at noon','정오에'),('at night','밤에'),('at the post office','우체국에서'),('at the airport','공항에서'),('at the hospital','병원에서'),('on Friday','금요일에'),('on March 8','3월 8일에'),('on the shelf','선반 위에'),('on the seventh floor','7층에'),('on the Web site','웹사이트에서')]
for i,(expr,k) in enumerate(time_place):
    add('전치사','in vs at vs on',f'The expression “{expr}” is closest in meaning to ______.',[k,'마감일까지','~에도 불구하고','~때문에'],0,
        f'“{expr}”는 “{k}”라는 뜻이다.',f'{expr}는 사진 표에 나온 자연스러운 시간·장소 전치사 결합입니다.',
        '나머지는 각각 종료시점·양보·원인을 나타내 이 표현의 의미가 아닙니다.',expr,'오전 사진 32쪽')

preps=[('within two weeks','2주 이내에'),('within 24 hours','24시간 이내에'),('within three months','3개월 이내에'),('within the company','회사 내에서'),('within the city limits','시 경계 안에서'),('throughout the last decade','지난 10년 내내'),('throughout the year','일 년 내내'),('throughout the workshop','워크숍 내내'),('throughout the handbook','안내서 곳곳에'),('throughout the building','건물 곳곳에'),('in front of the museum','박물관 앞에'),('behind the column','기둥 뒤에'),('under the table','테이블 아래에'),('above the floor','바닥 위쪽에'),('over the water','수면 위에'),('next to the fountain','분수대 옆에'),('beside the fountain','분수대 옆에'),('by the window','창가에'),('by the river','강가에'),('opposite the supermarket','슈퍼마켓 맞은편에'),('across from the supermarket','슈퍼마켓 맞은편에'),('between Maple Street and 7th Avenue','메이플가와 7번가 사이에'),('among new employees','신입 직원들 사이에'),('toward the airport','공항을 향해'),('into the new building','새 건물 안으로'),('along the border','국경을 따라'),('along the lane','차선을 따라'),('past the market','시장을 지나')]
for i,(expr,k) in enumerate(preps):
    add('전치사','전치사 의미 구별',f'The expression “{expr}” is closest in meaning to ______.',[k,'마감일까지','~때문에','~에도 불구하고'],0,f'“{expr}”는 “{k}”라는 뜻이다.',
        f'{expr}의 정확한 의미와 결합을 묻는 문제입니다.','나머지는 종료시점·원인·양보를 나타내 이 표현과 뜻이 다릅니다.',expr,'오전 사진 32~33쪽')

special=[('without','~없이'),('as','~로서'),('despite','~에도 불구하고'),('regarding','~에 관하여'),('except for','~를 제외하고'),('following','~후에'),('including','~를 포함하여'),('in addition to','~이외에도'),('due to','~때문에'),('in advance of','~전에'),('other than','~이외에도'),('prior to','~전에'),('owing to','~때문에'),('aside from','~를 제외하고/~이외에도'),('apart from','~를 제외하고/~이외에도'),('in spite of','~에도 불구하고'),('regardless of','~와 상관없이'),('instead of','~대신에'),('because of','~때문에')]
for i,(p,k) in enumerate(special):
    add('전치사','전치사 vs 접속사',f'The expression “{p}” is closest in meaning to ______.',[k,'~하는 동안','~라면','~할 수 있도록'],0,
        f'“{p}”는 “{k}”라는 뜻이다.',f'{p}는 뒤에 명사구를 받는 전치사(구)입니다.',
        '나머지는 시간·조건·목적을 나타내는 접속사 의미입니다.',f'{p} + 명사 = {k}', '오전 사진 34쪽')

conjs=[('if','~라면'),('provided that','~라면'),('providing that','~라면'),('unless','~가 아니라면'),('as long as','~하는 한'),('once','일단 ~하면'),('so that','~할 수 있도록'),('in order that','~할 수 있도록'),('whereas','~인 반면에'),('while','~인 반면에'),('as if','마치 ~인 것처럼'),('as though','마치 ~인 것처럼'),('as soon as','~하자마자'),('although','~에도 불구하고'),('though','~에도 불구하고'),('even if','비록 ~일지라도'),('even though','~에도 불구하고'),('because','~때문에'),('since','~때문에/~이래로'),('now that','이제 ~이므로'),('in case that','~의 경우에 대비하여'),('given that','~을 고려하면'),('considering that','~을 고려하면')]
for i,(c,k) in enumerate(conjs):
    add('접속사','전치사 vs 접속사',f'The conjunction “{c}” is closest in meaning to ______.',[k,'~에 관하여','~를 제외하고','~앞에'],0,
        f'접속사 “{c}”는 “{k}”라는 뜻이다.',f'{c}는 뒤의 주어+동사 절을 연결하는 접속사입니다.',
        '나머지는 전치사 의미이므로 절을 이끄는 이 접속사의 뜻과 다릅니다.',f'{c} + S + V = {k}', '오전 사진 35~36쪽')

reduced=[('when','submitting','제출할 때'),('while','reviewing','검토하는 동안'),('before','entering','들어가기 전에'),('after','checking','확인한 후'),('since','joining','입사한 이후로'),('when','approved','승인될 때'),('if','selected','선발된다면'),('unless','accompanied','동반되지 않는다면'),('as','discussed','논의된 대로'),('once','submitted','일단 제출되면'),('although','limited','제한적임에도')]
for i,(c,form,k) in enumerate(reduced):
    ing=form.endswith('ing')
    add('분사·축약절','-ing vs p.p.',f'{c.capitalize()} ______, the document should be saved immediately.',[form, 'submit' if ing else 'submitting','to submit','was submitted'],0,
        f'{k}, 그 문서는 즉시 저장되어야 한다.',f'주절과 주어가 같고 {"능동" if ing else "수동"} 관계이므로 {c} {form}으로 축약합니다.',
        '원형·to부정사·주어 없는 유한동사는 접속사 뒤의 축약절 형식에 맞지 않습니다.',f'{c} + {"V-ing" if ing else "p.p."}', '오전 사진 36~37쪽')

noun_conj=[('that','~라는 것'),('whether','~인지 아닌지'),('if','~인지 아닌지'),('who','누가 ~하는지'),('what','무엇을 ~하는지'),('which','어느 것이 ~하는지'),('when','언제 ~하는지'),('where','어디서 ~하는지'),('how','어떻게 ~하는지'),('why','왜 ~하는지')]
for i,(c,k) in enumerate(noun_conj):
    add('명사절','명사절 접속사',f'The noun-clause marker “{c}” is closest in meaning to ______.',[k,'~에도 불구하고','~하는 동안','~때문에'],0,
        f'명사절 표지 “{c}”는 “{k}”라는 뜻이다.',f'{c}가 뒤 절을 한 덩어리의 명사절로 만들어 주어·목적어·보어 역할을 하게 합니다.',
        '나머지는 양보·시간·원인의 부사 관계를 나타내 명사절 표지의 뜻이 아닙니다.',f'{c} + S + V = {k}', '오전 사진 37~38쪽')

# 기존 사이트의 핵심 문제은행: 의미·문장 중복 없이 개별 학습 포인트를 보존한다.
existing=[
('자·타동사/전치사','attend','Several representatives will ______ the annual trade conference in Busan.',['attend','attend to','participate','arrive'],0,'여러 대표들이 부산에서 열리는 연례 무역회의에 참석할 것이다.','attend는 행사·회의를 직접 목적어로 받는 타동사입니다.','attend to는 처리하다, participate는 in이 필요하고 arrive도 장소 전치사가 필요합니다.','attend a conference'),
('자·타동사/전치사','comply with','All employees must comply ______ the updated safety regulations.',['with','to','for','on'],0,'모든 직원은 갱신된 안전 규정을 준수해야 한다.','comply with가 고정 결합입니다.','to/for/on은 comply와 규정 대상을 연결하지 않습니다.','comply with regulations'),
('자·타동사/전치사','result in vs from','The new process resulted ______ lower operating costs.',['in','from','to','with'],0,'새 공정은 더 낮은 운영비를 가져왔다.','result in + 결과를 씁니다.','result from은 원인을 뒤에 두며 to/with는 이 동사와 결합하지 않습니다.','result in 결과 / result from 원인'),
('동사 형식','5형식','The board ______ Mr. Lee the new director.',['appointed','arrived','occurred','waited'],0,'이사회는 이 씨를 새 이사로 임명했다.','appoint + 목적어 + 목적격보어의 5형식입니다.','나머지는 자동사이거나 이 구조로 임명을 나타낼 수 없습니다.','appoint A B = A를 B로 임명하다'),
('수일치','each vs a number','Each of the applicants ______ a résumé.',['has submitted','have submitted','submit','submitting'],0,'지원자들은 각자 이력서를 제출했다.','each of + 복수명사는 단수 동사와 일치합니다.','복수 동사와 분사는 단수 주어 each에 맞지 않습니다.','each of + 복수명사 + 단수동사'),
('동사 시제','by + 미래','By next Friday, the team ______ the project.',['will have completed','completed','has completed','completes'],0,'다음 주 금요일까지 팀은 프로젝트를 완료해 놓을 것이다.','by + 미래 시점은 미래완료와 잘 어울립니다.','나머지 시제는 미래 기준점까지의 완료를 나타내지 못합니다.','by + 미래시점 → will have p.p.'),
('가산·불가산','information','We need additional ______ about the product.',['information','informations','an information','inform'],0,'우리는 그 제품에 관한 추가 정보가 필요하다.','information은 불가산명사입니다.','복수형·부정관사를 쓰지 않으며 inform은 동사입니다.','additional information'),
('복합명사','expense report','Please submit the ______ form by Friday.',['expense report','expense reporting','expenses report','report expense'],0,'금요일까지 경비 보고서 양식을 제출해 주세요.','expense report는 경비 보고서라는 복합명사입니다.','나머지는 관용적인 명사 결합이 아닙니다.','expense report form'),
('형용사·부사','부사 자리','Orders placed before noon are usually processed ______.',['promptly','prompt','promptness','prompting'],0,'정오 전에 접수된 주문은 보통 신속하게 처리된다.','processed를 수식하는 부사 promptly가 필요합니다.','prompt는 형용사, promptness는 명사, prompting은 현재분사입니다.','process promptly'),
('수량 표현','few vs little','Only ______ applicants met all requirements.',['a few','a little','much','every'],0,'소수의 지원자만 모든 요건을 충족했다.','복수 가산명사 applicants에는 a few를 씁니다.','a little/much는 불가산, every는 단수명사와 결합합니다.','a few + 복수 / a little + 불가산')]
for row in existing:add(*row)

# 문장과 선택지·정답 조합을 동시에 검사하여 중복 제거한다.
dedup=[]; seen_q=set(); seen_combo=set()
for q in items:
    qkey=re.sub(r'[^a-z0-9가-힣]+',' ',q['q'].lower()).strip()
    combo='|'.join(sorted(q['choices']))+'|'+q['choices'][q['answer']]
    # 선택지·정답 조합은 문장과 함께 동일할 때만 중복으로 본다. 서로 다른
    # 필수 표현을 같은 보기 형식으로 묻는 문항까지 버리면 사진 전수 반영이 깨진다.
    full_combo=qkey+'|'+combo
    if full_combo in seen_combo: continue
    seen_q.add(qkey); seen_combo.add(full_combo); dedup.append(q)

# 정답 위치는 A/B/C/D가 최대 1개 차이만 나도록 순환 배치한다.
for i,q in enumerate(dedup):
    target=i%4; old=q['answer']; ans=q['choices'][old]
    choices=[x for j,x in enumerate(q['choices']) if j!=old]
    choices.insert(target,ans); q['choices']=choices; q['answer']=target; q['id']=f'q{i+1:04d}'

(ROOT/'questions.js').write_text('window.QUESTIONS='+json.dumps(dedup,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(json.dumps({"questions":len(dedup),"categories":{c:sum(x['category']==c for x in dedup) for c in sorted(set(x['category'] for x in dedup))},"answers":[sum(x['answer']==i for x in dedup) for i in range(4)]},ensure_ascii=False,indent=2))
