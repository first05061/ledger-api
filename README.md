# 가계부 API (FastAPI + Supabase PostgreSQL)

- GitHub: https://github.com/first05061/ledger-api
- Render: https://ledger-api-ytfq.onrender.com (API 문서: /docs)

## 엔드포인트
- POST /accounts · GET /accounts · GET /accounts/{account_id}
- POST /transactions · GET /accounts/{account_id}/detail
- GET /stats/by-category

## 실습 기록
### ① 결과 확인
(Supabase Table Editor 캡처, Render /docs GET /accounts 캡처)

### ② 핵심 개념 되새김
- 계좌·거래를 두 테이블로 나눈 이유(1:N):
- SQLAlchemy 모델 클래스와 테이블의 대응:
- 접속 문자열을 .env로 분리하는 이유:

### ③ 자유 로그
- AI에게 시킨 것과 검증 방법:
