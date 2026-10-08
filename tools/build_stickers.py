# -*- coding: utf-8 -*-
"""Build stickers.html from stickers.src.html + assets/stickers/<pack>/*.png.

Usage: python tools/build_stickers.py
Pack order, names and per-sticker labels live in PACKS below; files are read from disk.
"""
import io, json, os
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS = [
    ('capy', '카피바라 캐릭터', ['인사','책 읽기','필기','질문','엄지 척','박수','생각 중','아이디어','축하','하트','쉬는 중','응원']),
    ('icons', '수업 아이콘', ['연필','책','전구','시계','돋보기','체크','별','트로피','지구본','계산기','물음표','하트']),
    ('subjects', '과목·학교생활', ['국어','수학','과학','사회','영어','음악','미술','체육','정보','급식','가방','학교']),
    ('labels', '문구 배지', ['참 잘했어요','중요!','정답','다시 보기','시험에 나와요','꼭 기억!','오늘의 목표','질문 있어요?','모둠 활동','발표 시간','쉬는 시간','복습하기']),
    ('emoji', '이모티콘', ['웃음','윙크','하트 눈','놀람','생각 중','엄지 척','박수','울먹임','화남','졸림','축하','아이디어']),
    ('ppt', 'PPT 꾸미기', ['1','2','3','4','5','오른쪽 화살표','곡선 화살표','양방향 화살표','말풍선','생각 풍선','제목 리본','메모지','체크박스','형광펜','반짝임']),
    ('callig', '캘리그라피', ['참 잘했어요','수고했어요','고맙습니다','사랑합니다','힘내요','할 수 있어!','새 학기 새 출발','축 졸업','스승의 은혜 감사합니다','꿈을 향해','오늘도 행복하게','함께라서 좋아요']),
    ('buttons', 'PPT 버튼', ['시작하기','다음','이전','처음으로','정답 확인','다시 하기','힌트','퀴즈 시작','결과 보기','O','X','재생','일시정지','소리','메뉴']),
    ('animals', '귀여운 동물', ['강아지','고양이','토끼','곰','판다','펭귄','여우','다람쥐','병아리','코끼리','고슴도치','수달']),
    ('phrases', '학습자료 문구', ['학습 목표','핵심 개념','생각해 보기','함께 해 봐요','확인 문제','정리하기','더 알아보기','주의!','예시','탐구 활동','오늘 배운 것','스스로 평가']),
    ('official', '공식 그래픽', ['확인 도장','메달 리본','졸업','월계관','공지','체크리스트','달력','편지','인증 배지','만년필','학교','악수']),
    ('lineicons', '라인 아이콘', ['집','학생','모둠','말풍선','메일','전화','위치','시계','달력','카메라','영상','음악','다운로드','링크','검색','설정','자물쇠','휴지통','편집','별']),
    ('anime', '애니 캐릭터', ['질문','칠판','독서','토론','박수','엄지 척','고민','아이디어','발표','시험 공부','응원','인사']),
]
ORDER = ['capy','animals','anime','callig','phrases','buttons','labels','official','icons','lineicons','ppt','subjects','emoji']
PREVIEW = {'capy':[0,3,8,11],'callig':[0,2,4,7],'buttons':[0,4,9,10],'labels':[0,1,2,4],'icons':[2,6,7,8],'ppt':[0,5,8,10],'subjects':[0,2,5,6],'emoji':[0,2,5,10],'animals':[0,1,2,4],'phrases':[0,1,4,5],'official':[0,1,2,8],'lineicons':[0,3,8,14],'anime':[0,2,7,8]}
PACKS.sort(key=lambda p: ORDER.index(p[0]) if p[0] in ORDER else 99)
out = []
for key, name, labels in PACKS:
    d = os.path.join(ROOT, 'assets', 'stickers', key)
    if not os.path.isdir(d): continue
    files = sorted(f for f in os.listdir(d) if f.endswith('.png'))
    items = []
    for i, f in enumerate(files):
        w, h = Image.open(os.path.join(d, f)).size
        items.append({'file': f, 'w': w, 'h': h, 'label': labels[i] if i < len(labels) else ''})
    out.append({'key': key, 'name': name, 'dir': f'assets/stickers/{key}', 'items': items, 'preview': PREVIEW.get(key, [0, 1, 2, 3])})
src = io.open(os.path.join(ROOT, 'stickers.src.html'), encoding='utf-8').read()
io.open(os.path.join(ROOT, 'stickers.html'), 'w', encoding='utf-8', newline='\n').write(src.replace('__PACKS__', json.dumps(out, ensure_ascii=False)))
print('packs', [(p['key'], len(p['items'])) for p in out])
