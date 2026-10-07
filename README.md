# 배움의 도구 · 교사·학생용 GPT 이미지 프롬프트 생성기

학생·선생님이 **예시 그림을 고르고 학년·과목·주제만 입력하면** ChatGPT에 바로 붙여넣을 수 있는
학습 이미지 생성 프롬프트가 완성되는 웹페이지입니다. 서버·API 키·설치 없이 브라우저만 있으면 됩니다.

**사이트 주소:** https://gambit133.github.io/gpt_prompt/

## 사용 방법

1. **1. 어떤 자료를 만들까요?** 첫 화면에는 예시 그림만 보입니다. 탭(정리·이해·암기·점검·선생님용)과 스타일 필터·검색으로 좁힌 뒤 그림을 누르면
   큰 팝업에서 **어떤 자료인지**, **이럴 때 좋은지**를 확인하고 ‹ › 로 옆 예시를 넘겨 볼 수 있습니다. **이 그림으로 만들기**를 누르면 편집 화면으로 바뀝니다.
2. 편집 화면 왼쪽에는 선택한 예시가 크게, 아래에 같은 묶음의 다른 후보가 띠로 나옵니다. 오른쪽(모바일은 아래)에서 **2. 간단히 적기**의 학년·과목·주제(필수, 빨간 * 표시)를 적고,
   필요하면 **세부 조정**에서 톤·색감·글꼴·삽화·글자량·비율·언어를 고릅니다. 고른 항목만 프롬프트의 [세부 조정]에 들어갑니다.
3. **다음 → 프롬프트 확인**을 누르면 **3. 복사해서 붙여넣기**가 강조됩니다. **프롬프트 복사**와 **예시 이미지 복사**를 눌러 ChatGPT에 붙여넣고, 자료가 있으면 함께 첨부합니다.

현재 진행 중인 단계는 테두리가 은은하게 깜빡이며 강조되고, 아직 차례가 아닌 단계는 흐리게 표시됩니다.

- 주제에 **구운몽**(국어)을 적으면 예시 이미지를 실제로 만들 때 쓴 상세 지시문이 그대로 사용됩니다.
- 선생님용 그림을 고르면 교사용 지시가 자동으로 붙습니다.

### 자료를 첨부하면 알아서 정리합니다

ChatGPT 입력창의 **+** 버튼으로 교과서·필기 사진, 학습지, 요약본, PDF·한글 문서, 수업 PPT 등을 올리고 이 프롬프트를 붙여넣으면
자료의 핵심을 뽑아 선택한 형식으로 정리합니다. 프롬프트에는 다음 지시가 들어 있습니다.

- 첨부 자료의 용어·표기·순서·강조점을 그대로 우선 사용
- 자료가 여러 개면 겹치는 내용은 합치고, 자료에 없는 보충 내용은 '보충'으로 표시
- 글씨가 흐릿하거나 범위가 불분명하면 만들기 전에 먼저 질문
- 참고 이미지는 손글씨·형광펜 스타일의 기준으로만 사용

**ChatGPT에 자료를 첨부할게요** 체크를 끄면 첨부 없이 교과서 수준의 일반 내용으로 만들도록 바뀝니다.
예시마다 손글씨·인포그래픽·코넬 노트·칠판·만화·플래시카드 등 시각 스타일이 다르며, 프롬프트의 [스타일] 항목이 선택한 예시에 맞게 바뀝니다.

### 예시 이미지를 함께 첨부하면 더 정확합니다

프롬프트에는 글로 쓴 구성·스타일 설명이 들어가지만, 그림을 직접 보여 주는 쪽이 배치와 색감을 훨씬 잘 따라갑니다.
**예시 이미지 복사**를 누른 뒤 ChatGPT 입력창에 Ctrl+V(⌘V)로 붙여넣고 이어서 프롬프트를 붙여넣으세요.
프롬프트의 [예시 이미지 참고] 항목이 "첨부한 예시와 같은 구성·배치·스타일을 유지하고 내용만 새 주제로 바꾸라"고 지시합니다.
이미지 복사가 안 되는 기기에서는 **예시 이미지 저장**으로 받은 파일을 첨부하면 됩니다.

주제에 **구운몽**(국어)을 적으면 예시 이미지를 실제로 만들 때 쓴 상세 지시문이 그대로 사용됩니다.

## 예시 이미지

| 역할 | 예시 유형 | 프롬프트 구분 | 이미지 |
| --- | --- | --- | --- |
| 학습용 | 상세 학습 노트 | 상세 · 실제 생성 지시 | [assets/s-notes.jpg](assets/s-notes.jpg) |
| 학습용 | 환몽 구조도 | 상세 · 실제 생성 지시 | [assets/s-map.jpg](assets/s-map.jpg) |
| 학습용 | 암기 카드 | 기본 · 재현용 지시 | [assets/s-cards.jpg](assets/s-cards.jpg) |
| 학습용 | 선지 판단 | 기본 · 재현용 지시 | [assets/s-judgment.jpg](assets/s-judgment.jpg) |
| 학습용 | 손글씨 학습 노트 | 상세 · 생성 지시 | [assets/s-hand.jpg](assets/s-hand.jpg) |
| 학습용 | 포스트잇 요약 | 상세 · 생성 지시 | [assets/s-postit.jpg](assets/s-postit.jpg) |
| 학습용 | 개념 시각화 | 상세 · 생성 지시 | [assets/s-visual.jpg](assets/s-visual.jpg) |
| 학습용 | 단원 요약하기 | 상세 · 생성 지시 | [assets/s-summary.jpg](assets/s-summary.jpg) |
| 학습용 | 기초 개념 확인하기 | 상세 · 생성 지시 | [assets/s-basics.jpg](assets/s-basics.jpg) |
| 학습용 | 쉽게 설명하기 | 상세 · 생성 지시 | [assets/s-explain.jpg](assets/s-explain.jpg) |
| 학습용 | 일상생활에 비유하기 | 상세 · 생성 지시 | [assets/s-analogy.jpg](assets/s-analogy.jpg) |
| 학습용 | 원리 이해하기 | 상세 · 생성 지시 | [assets/s-principle.jpg](assets/s-principle.jpg) |
| 학습용 | 헷갈리는 개념 비교 | 상세 · 생성 지시 | [assets/s-compare.jpg](assets/s-compare.jpg) |
| 학습용 | 반례와 적용 조건 찾기 | 상세 · 생성 지시 | [assets/s-counter.jpg](assets/s-counter.jpg) |
| 학습용 | 오개념 바로잡기 | 상세 · 생성 지시 | [assets/s-misconception.jpg](assets/s-misconception.jpg) |
| 학습용 | 실제 사례 연결하기 | 상세 · 생성 지시 | [assets/s-realcase.jpg](assets/s-realcase.jpg) |
| 학습용 | 질문으로 이해하기 | 상세 · 생성 지시 | [assets/s-socratic.jpg](assets/s-socratic.jpg) |
| 학습용 | 내 설명 점검하기 | 상세 · 생성 지시 | [assets/s-selfcheck.jpg](assets/s-selfcheck.jpg) |
| 학습용 | 풀이 과정 이해하기 | 상세 · 생성 지시 | [assets/s-solving.jpg](assets/s-solving.jpg) |
| 학습용 | 근거 기반 예상문제 | 상세 · 생성 지시 | [assets/s-questions.jpg](assets/s-questions.jpg) |
| 학습용 | 한 장 복습 자료 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-onepage.jpg](assets/s-onepage.jpg) |
| 학습용 | 코넬 노트 만들기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-cornell.jpg](assets/s-cornell.jpg) |
| 학습용 | 용어 사전 만들기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-glossary.jpg](assets/s-glossary.jpg) |
| 학습용 | 공식 정리하기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-formula.jpg](assets/s-formula.jpg) |
| 학습용 | 시간순 정리하기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-timeline.jpg](assets/s-timeline.jpg) |
| 학습용 | 과정 단계별 정리 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-process.jpg](assets/s-process.jpg) |
| 학습용 | 비교표 만들기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-comparetable.jpg](assets/s-comparetable.jpg) |
| 학습용 | 핵심 내용 추리기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-keypoints.jpg](assets/s-keypoints.jpg) |
| 학습용 | 암기 카드 만들기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-flashcards.jpg](assets/s-flashcards.jpg) |
| 학습용 | 두문자 암기법 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-acronym.jpg](assets/s-acronym.jpg) |
| 학습용 | 이야기로 외우기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-story.jpg](assets/s-story.jpg) |
| 학습용 | 묶어서 외우기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-chunk.jpg](assets/s-chunk.jpg) |
| 학습용 | 빈칸 문제 만들기 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-blanks.jpg](assets/s-blanks.jpg) |
| 학습용 | 기억 꺼내기 연습 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-retrieval.jpg](assets/s-retrieval.jpg) |
| 학습용 | 기억한 내용 점검 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-recallcheck.jpg](assets/s-recallcheck.jpg) |
| 학습용 | 요약 정확성 확인 | 상세 · 생성 지시 (다양한 스타일) | [assets/s-summarycheck.jpg](assets/s-summarycheck.jpg) |
| 선생님 | 50분 수업 지도안 | 상세 · 실제 생성 지시 | [assets/t-plan.jpg](assets/t-plan.jpg) |
| 선생님 | 학생 활동 학습지 | 상세 · 실제 생성 지시 | [assets/t-sheet.jpg](assets/t-sheet.jpg) |
| 선생님 | 형성평가 | 기본 · 재현용 지시 | [assets/t-quiz.jpg](assets/t-quiz.jpg) |
| 선생님 | 서술형 채점 기준 | 기본 · 재현용 지시 | [assets/t-rubric.jpg](assets/t-rubric.jpg) |
| 선생님 | 학습 목표 만들기 | 상세 · 생성 지시 (다양한 스타일) | [assets/t-goals.jpg](assets/t-goals.jpg) |
| 선생님 | 수업 흐름 간단 설계 | 상세 · 생성 지시 (다양한 스타일) | [assets/t-flow.jpg](assets/t-flow.jpg) |
| 선생님 | 핵심 발문 만들기 | 상세 · 생성 지시 (다양한 스타일) | [assets/t-questions.jpg](assets/t-questions.jpg) |
| 선생님 | 선수학습 진단 | 상세 · 생성 지시 (다양한 스타일) | [assets/t-diagnosis.jpg](assets/t-diagnosis.jpg) |

## 파일 구성

| 파일 | 설명 |
| --- | --- |
| `index.html` | 웹페이지 본체(약 230KB). 예시 데이터와 프롬프트가 들어 있고, 이미지는 `assets/`에서 지연 로딩합니다. |
| `.nojekyll` | GitHub Pages가 Jekyll 처리 없이 파일을 그대로 서빙하도록 합니다. |
| `assets/` | 예시 이미지 44종(JPG), 갤러리용 썸네일(`thumbs/`), 상세 예시 4종의 고해상도 PNG. 노션 등에 올릴 때 개별 파일로 사용합니다. |
| `reference.jpg` | 초기 손글씨 스타일 참고 이미지(현재 페이지에서는 선택한 예시 이미지를 대신 저장합니다). |
| `구운몽-이미지-프롬프트.md` | 예시 이미지 8종을 실제 생성·재현하는 데 사용한 프롬프트 정리본 |
| `통합-노션-프롬프트.md` | 학생용 55종·교사용 35종 텍스트 프롬프트 원문 모음(참고용, 웹페이지에는 포함하지 않음) |
| `교사용-구운몽-학습지-정답.md` | 학생 활동 학습지의 교사용 정답과 지도 참고 |
| `image-index.csv` | 예시 이미지 목록 |
| `.github/workflows/pages.yml` | GitHub Pages 자동 배포 워크플로 |

## GitHub Pages 배포

이 저장소는 **GitHub Actions**로 Pages를 배포합니다.

1. `Settings → Pages → Build and deployment → Source`를 **GitHub Actions**로 선택합니다.
   (워크플로 첫 실행 시 자동 설정을 시도하지만, 실패하면 직접 선택해 주세요.)
2. `main` 브랜치에 푸시하면 워크플로가 실행되고, 끝나면 `Actions` 탭 또는 `Settings → Pages`에서 주소를 확인할 수 있습니다.
3. 수정은 `index.html`을 고쳐 커밋·푸시하면 됩니다.

워크플로 없이 쓰려면 `Source`를 **Deploy from a branch**로 바꾸고 `main` / `/ (root)`를 선택해도 됩니다.
`index.html`이 저장소 최상위에 있으므로 그대로 동작합니다.

## 로컬에서 열기

`index.html`을 더블클릭해 브라우저로 열면 됩니다. 이미지는 같은 폴더의 `assets/`에서 읽으므로 폴더째 두세요.

## 안내

- 웹페이지는 프롬프트를 **작성**만 합니다. 실제 답변과 이미지는 ChatGPT에 붙여넣어 생성합니다.
- 입력한 내용은 저장되거나 서버로 전송되지 않습니다.
- 예시 이미지와 해석은 참고 자료이며, 실제 수업 지문과 학교 평가 기준에 맞춰 확인하세요.
- 문학 개념 참고: [한국민족문화대백과사전 「구운몽」](https://encykorea.aks.ac.kr/Article/E0005948)
