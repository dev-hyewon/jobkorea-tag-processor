# 🏷️ JobKorea Tag Processor (with LangGraph)

잡코리아(JobKorea) 채용 공고에서 태그를 수집하고, LangGraph 기반 LLM 파이프라인으로 정제 및 군집화하는 자동화 시스템입니다.

## 📌 주요 기능

- ✅ 잡코리아 채용 공고에서 태그 데이터 크롤링
- ✅ 중복, 불필요 단어 제거를 통한 태그 정제
- ✅ LLM을 활용한 유사 태그 군집화 및 요약
- ✅ LangGraph 기반 상태 머신(flow)로 처리 흐름 구성
- ✅ 조건 분기 및 validation 로직 적용 가능 (Human-in-the-loop 확장 가능)

<br/> <br/>  
---
<br/> <br/> 

## 🧱 프로젝트 구조

```bash
jobkorea-tag-processor/
├── README.md
├── requirements.txt
├── .env                         # API 키 등 환경 변수
├── run.py                      # 메인 실행 스크립트
│
├── crawler/
│   └── jobkorea_crawler.py     # 잡코리아에서 채용 정보 및 태그 수집
│
├── preprocessor/
│   └── tag_cleaner.py          # 수집된 태그 정제, 중복 제거 등
│
├── langgraph_pipeline/
│   ├── __init__.py
│   ├── tag_cluster_node.py     # 태그 유사도 기반 군집화 (LLM 기반)
│   ├── tag_summary_node.py     # 대표 키워드 요약 또는 설명 생성
│   ├── validation_node.py      # 결과 품질 검사 및 조건 분기
│   └── graph_builder.py        # 전체 LangGraph state machine 정의
│
├── data/
│   └── raw_data.json           # 수집된 원시 데이터 샘플
│   └── processed_data.json     # 처리 완료된 결과 저장
│
└── utils/
    └── logger.py               # 로깅 및 유틸 함수

```
<br/> <br/> 

## 🚀 실행 방법

### 1. 환경 구성

```bash
git clone https://github.com/yourname/jobkorea-tag-processor.git
cd jobkorea-tag-processor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
<br/>   

### 2. 환경 변수 설정

.env 파일 생성 후 아래와 같이 설정 (예: OpenAI API 사용 시)
```ini
OPENAI_API_KEY=sk-...
```
<br/> 

### 3. 실행

```
python run.py
```
실행 후 data/processed_data.json에 결과가 저장됩니다.
<br/> <br/> 

## 🧠 LangGraph 흐름 구성

```markdown
        ┌────────────┐
        │  태그 정제  │
        └─────┬──────┘
              ▼
     ┌──────────────────┐
     │ LLM 태그 군집화 노드 │
     └─────┬────────────┘
           ▼
    ┌──────────────────┐
    │ 태그 요약/대표 추출 │
    └─────┬────────────┘
          ▼
    ┌──────────────────┐
    │ 품질 검사 및 분기 │
    └──────────────────┘
```
LangGraph를 사용하여 **분기, 상태 공유, 모듈 조합형 흐름을 학습할 수 있습니다.
<br/> <br/> 

## 🛠️ 사용 기술

- Python 3.9+
- LangGraph
- LangChain
- OpenAI GPT (또는 로컬 모델로 대체 가능)
- BeautifulSoup4 (웹 크롤링)
- dotenv (환경 변수)
<br/> <br/> 

## 📈 향후 확장 아이디어

- 🔄 LangGraph 내에서 Human Feedback Loop 추가
- 🗃️ 결과를 DB(SQlite/PostgreSQL 등)에 저장
- 📊 태그 트렌드 시각화 대시보드 연동
- 🧠 Ollama 등 로컬 모델 연동 (로컬 환경에서 실행 가능하게)
<br/> <br/> 

## 🙋‍♂️ 만든 사람
https://github.com/dev-hyewon