from sqlalchemy import create_engine ## creates a lazy connnection that can conncect when query is executed
# if not orm
#import mysql.connector
from sqlalchemy.ext.declarative import declarative_base 
# base class to map python class to sql tables
from sqlalchemy.orm import sessionmaker

"""
if not ORM SQLAlchemy
def get_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="testdb"  ##this is what that we creared db

    )


"""

# Replace with your MySQL credentials  using ORM
DATABASE_URL = "mysql+pymysql://root:mysql@localhost/testdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#flush it means that it sends to db but not saved permanently

Base = declarative_base()
