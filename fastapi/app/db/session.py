from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# 일단 디폴트 설정으로 생성
# https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine
# 기본적으로 connection pool에 5개의 인스턴스 생성
# echo=True 설정시 쿼리 확인 가능(default : False)
print("123123123121231")
print(settings.SQLALCHEMY_DATABASE_URI, flush=True)
engine = create_engine('mysql+pymysql://root:password@db:3306/fasttest', pool_pre_ping=True)

# SessionLocal로 이름을 지정한 이유는 추후에 사용할 Session과 분리하기 위함
# SessionLocal은 DB session을 생성하는 factory
SessionLocal = sessionmaker(bind=engine)