from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///sales.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)