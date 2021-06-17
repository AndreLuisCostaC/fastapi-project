from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQKALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQKALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

# db_name: db_course
# user: andre
# pwd andre1