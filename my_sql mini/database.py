from sqlalchemy import create_engine ## creates a lazy connnection that can conncect when query is executed

from sqlalchemy.ext.declarative import declarative_base 
# base class to map python class to sql tables
from sqlalchemy.orm import sessionmaker

# Replace with your MySQL credentials
DATABASE_URL = "mysql+pymysql://root:mysql@localhost/testdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#flush it means that it sends to db but not saved permanently

Base = declarative_base()
