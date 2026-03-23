from pydantic import BaseModel
from typing import Optional, List

class Student(BaseModel):
    name:str
    email:Optional[str]
    course:str
    age:int

class ShowStudent(Student):
    id:int