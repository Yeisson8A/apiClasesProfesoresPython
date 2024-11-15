from sqlalchemy.orm import Session
from models.models import Teacher, Class
from schemas.schemas import TeacherSchema

def get_teachers(db:Session):
    return db.query(Teacher).all()

def get_teacher_by_id(db:Session, id:int):
    return db.query(Teacher).filter(Teacher.id == id).first()

def get_teacher_by_id_with_classes(db:Session, id:int):
    return db.query(Teacher).filter(Teacher.id == id).one_or_none()

def create_teacher(db:Session, teacher:TeacherSchema):
    _teacher = Teacher(name = teacher.name)
    db.add(_teacher)
    db.commit()
    db.refresh(_teacher)
    return _teacher

def remove_teacher(db:Session, id:int):
    _teacher = get_teacher_by_id(db=db,id=id)

    if _teacher is None:
        raise Exception(f"Teacher with id {id} not exist")

    db.delete(_teacher)
    db.commit()
    return _teacher

def update_teacher(db:Session, id:int, name:str):
    _teacher = get_teacher_by_id(db=db, id=id)

    if _teacher is None:
        raise Exception(f"Teacher with id {id} not exist")

    _teacher.name = name
    db.commit()
    db.refresh(_teacher)
    return _teacher