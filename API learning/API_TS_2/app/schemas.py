from pydantic import BaseModel,Field
from typing import Optional, List

class StudentBase(BaseModel):
    name: str
    age: int
    student_class: str
    rollno: str
    teacher_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int

    class Config:
        orm_mode = True


class TeacherBase(BaseModel):
    name: str  = Field(...)
    last: str = Field(...)
    age: int = Field(...)
    subject: str = Field(...)

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    teacher_id: int
    students: Optional[List[Student]] = []

    class Config:
        orm_mode = True
