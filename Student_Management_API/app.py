from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from database import get_db, engine
import schema
from model import Student
from sqlalchemy.orm import Session
from schema import Base

Base.metadata.create_all(engine)

app = FastAPI(
    title="Student Management API"
)



@app.get('/')
def home():
    return {"message": "Welcome to Student Management API...🚀"}

@app.post('/student')
def add_student(req_body: Student, db: Session = Depends(get_db)):
    if req_body.age < 0 or len(req_body.name) < 3:
        return JSONResponse(
            status_code=409,
            content={"message":"Data validation error."}
        )
    student_in_db = db.query(schema.Student).filter(schema.Student.email == req_body.email).first()
    if student_in_db:
        return JSONResponse(
            status_code=409,
            content={"message":"Student already exists."}
        )
    student = schema.Student(
        name=req_body.name,
        email=req_body.email,
        course=req_body.course,
        age=req_body.age
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get('/student')
def get_all_student(db: Session = Depends(get_db)):
    students =  db.query(schema.Student).all()
    return students

@app.get('/student/{id}')
def get_student(id:int, db: Session = Depends(get_db)):
    student = db.query(schema.Student).filter(schema.Student.id == id).first()
    if not student:
        return JSONResponse(
            status_code=404,
            content={"content": "Student not found."}
        )
    return student

@app.delete('/student/{id}')
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(schema.Student).filter(schema.Student.id == id).first()
    if not student:
        return JSONResponse(
            status_code=404,
            content={"message": "Student not found."}
        )
    db.delete(student)
    db.commit()
    return student
    

@app.put('/student')
def update_student(req_body: Student, db: Session = Depends(get_db)):
    student_in_db = db.query(schema.Student).filter(schema.Student.email == req_body.email).first()
    if not student_in_db:
        return JSONResponse(
            status_code=404,
            content={"message":"Student not found."}
        )
    student_in_db.name=req_body.name
    student_in_db.email=req_body.email
    student_in_db.course=req_body.course
    student_in_db.age=req_body.age
    db.commit()
    db.refresh(student_in_db)
    return student_in_db