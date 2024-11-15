from sqlalchemy import String, Column,Integer,ForeignKey
from db.config import Base
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(225), index=True, nullable=False)
    classes = relationship("Class", back_populates="teacher", cascade="all, delete-orphan")

class Class(Base):
    __tablename__='classes'
    id= Column(Integer,primary_key=True, index=True)
    name = Column(String(225), index=True, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="classes")