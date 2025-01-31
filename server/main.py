from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

app = FastAPI()

DATABASE_URL = 'postgresql+psycopg2://postgres:ali%241000@localhost:5432/fluttermusicapp'

engine=create_engine(DATABASE_URL)

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind= engine)

db= SessionLocal ()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

Base = declarative_base()

class User(Base):

@app.post('/signup')
def signup_user(user: UserCreate):
    print(user.name)
    print(user.email)
    print(user.password)
    
    pass 
    
     

