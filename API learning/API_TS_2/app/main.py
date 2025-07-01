from fastapi import FastAPI, APIRouter, Depends, HTTPException,Form,Request
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal
from . import models
from .database import engine


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



models.Base.metadata.create_all(bind=engine)



tags_metadata=[

    {"name":"Students",
    "description":"End points for Student"},

    {"name":"Teachers",
    "description":"End points for Teacher"}
]
from fastapi.responses import JSONResponse
app = FastAPI()

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )



# TEACHER

# CREATE TEACHER
@app.post("/teacher", response_model=schemas.Teacher,tags=["Teacher"])
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    #if schemas.TeacherCreate Agar validation fail ho: ❌ 422 error return karta hai
    if not any(teacher.dict().values()):
        raise HTTPException(status_code=422,detail="Data is missing")
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)    
    return db_teacher

# GET All Teachers
@app.get("/teachers", response_model=list[schemas.Teacher],tags=["Teacher"])
def get_teachers_without_students(db: Session = Depends(get_db)):
    subquery = db.query(models.Student.teacher_id).distinct()
    return db.query(models.Teacher).filter(
        ~models.Teacher.teacher_id.in_(subquery)
    ).all()

# GET ALL STUDENTS OF THE TEACHER on given id
@app.get("/students/{teacher_id}", response_model=list[schemas.Teacher],tags=["Teacher"])
def get_student_of_teacher(teacher_id:int,db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.teacher_id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail = "Teacher does not exists")
    students = db.query(models.Student.student_id).filter(models.Student.teacher_id == teacher_id).all()
    if not students:
        raise HTTPException(status_code=404, detail = "No Student is associated")

    return students


# DELETE Teacher (warning: deletes students too)
@app.delete("/teacher/{teacher_id}",tags=["Teacher"])
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.teacher_id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(teacher)
    db.commit()
    return {"message": "Teacher and associated students deleted"}




# # POST Student
@app.post("/student", response_model=schemas.Student,tags=["Student"])
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # t_id= student.dict().values()[4]
    # t_id = student.teacher_id
    teacher = db.query(models.Teacher).filter(models.Teacher.teacher_id == student.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/student", tags=["Student"])
def get_all_students(db: Session = Depends(get_db)):
    # students = db.query(models.Student.student_id).filter(models.Student.teacher_id == teacher_id).all()
    students = db.query(models.Student).all()
    return students

# DELETE Student
@app.delete("/student/{student_id}",tags=["Student"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}


