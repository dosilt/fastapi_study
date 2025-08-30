# FastAPI Study

FastAPI 학습을 위한 프로젝트입니다.

- window에서 uv 설치법
  - winget install astral-sh.uv (powershell에서 실행)

## 프로젝트 구조

```
FastAPI_Study/
├── script/
│   ├── fastapi_tutorial/          # FastAPI 공식 튜토리얼 학습
│   │   ├── main.py               # 클라이언트 테스트 코드
│   │   └── tutorial/
│   │       ├── 01_first_steps.py       # 기본 FastAPI 앱
│   │       ├── 02_path_parameters.py   # Path Parameters 예제
│   │       └── 03_query_parameters.py  # Query Parameters 예제
│   └── jump_to_fastapi/          # Jump to FastAPI 책 예제
│       └── chapter2/             # 2장: 데이터베이스 연동
└── README.md
```

## 설치 및 실행

### 1. 의존성 설치
```bash
uv sync
```

### 2. FastAPI 서버 실행
```bash
# 각 튜토리얼 파일을 직접 실행
python script/fastapi_tutorial/tutorial/01_first_steps.py
python script/fastapi_tutorial/tutorial/02_path_parameters.py
```

### 3. 클라이언트 테스트
```bash
# 서버 실행 후 별도 터미널에서
python script/fastapi_tutorial/main.py
```

## 학습 내용

### FastAPI Tutorial
- **01_first_steps.py**: 기본 FastAPI 애플리케이션 생성
- **02_path_parameters.py**: Path Parameters, 타입 힌트, Enum 사용법
- **03_query_parameters.py**: Query Parameters (예정)

### Jump to FastAPI
- **Chapter 2**: SQLAlchemy를 이용한 데이터베이스 연동

## 주요 기능

- FastAPI를 이용한 REST API 개발
- Path Parameters와 Query Parameters 처리
- 타입 힌트를 이용한 자동 검증
- Enum을 이용한 제한된 값 처리
- SQLAlchemy를 이용한 데이터베이스 연동

## 기술 스택

- **FastAPI**: 현대적이고 빠른 Python 웹 프레임워크
- **Uvicorn**: ASGI 서버
- **SQLAlchemy**: Python ORM
- **Requests**: HTTP 클라이언트 라이브러리
