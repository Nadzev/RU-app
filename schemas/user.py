from pydantic import BaseModel


class User(BaseModel):
    matricula: str
    name:   str
    age: int
    credits: int
    
    