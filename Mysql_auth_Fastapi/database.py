from sqlalchemy import create_engine ## to create connection to database
from sqlalchemy.ext.declarative import declarative_base #declarative class is a base  class for orm models,
#allows to crete python classes that mapp to databases tables
from sqlalchemy.orm import sessionmaker #session maker helps to create session objects to interact with db
import os #python os module to access envirnamental vairables(os.getenv())
from dotenv import load_dotenv 
## Loads environment variables from a .env file into your environment so they can be accessed os.getenv()
load_dotenv()  ## to load url from .env
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)  ##db connector
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()