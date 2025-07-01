from fastapi import FastAPI, HTTPException
from .database import db
from .models import Student
from .schemas import StudentCreate, Student as StudentSchema

app = FastAPI()

@app.on_event("startup")
def startup():
    if db.is_closed():
        db.connect()
    db.create_tables([Student])

@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()

@app.post("/students", response_model=StudentSchema)
def create_student(student: StudentCreate):
    student_obj = Student.create(**student.dict())
    return student_obj

@app.get("/students", response_model=list[StudentSchema])
def get_students():
    return list(Student.select())
