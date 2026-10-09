import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()   # .env를 읽어 환경변수로 등록
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ledger.db")

kwargs = {"echo": True}   # 실행되는 SQL을 콘솔에 출력
if DATABASE_URL.startswith("sqlite"):
    kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, **kwargs)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
