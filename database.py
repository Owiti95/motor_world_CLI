#a database.py file to establish a connection with the sales.db by creating an engine and defining a session factory to manage database transactions

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///your_database.db"

engine = create_engine(DATABASE_URL, echo=True)
# 'echo=True' enables SQL query logging for debugging purposes
# Creating a new SQLAlchemy engine, which will be used to interact with the database


#create a session factory attached to the engine
Session = sessionmaker(bind=engine)#interact with the database and perform CRUD operations


