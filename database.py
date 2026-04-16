from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:1234@localhost:5433/postgres"
engine = create_engine(db_url)

session = sessionmaker(autocommit = False,autoflush=False,bind=engine)