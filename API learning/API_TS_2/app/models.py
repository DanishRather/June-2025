from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    last = Column(String)
    age = Column(Integer)
    subject = Column(String)
    students = relationship("Student", back_populates="teacher", cascade="all, delete")

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    student_class = Column(String)
    rollno = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))
    teacher = relationship("Teacher", back_populates="students")
