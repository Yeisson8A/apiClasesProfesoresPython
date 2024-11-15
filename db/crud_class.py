from sqlalchemy.orm import Session
from models.models import Class
from schemas.schemas import ClassSchema

def get_classes(db:Session):
    return db.query(Class).all()

def get_class_by_id(db:Session, id:int):
    return db.query(Class).filter(Class.id == id).first()

def create_class(db:Session, cl:ClassSchema):
    _class = Class(name = cl.name, teacher_id = cl.teacher_id)
    db.add(_class)
    db.commit()
    db.refresh(_class)
    return _class

def remove_class(db:Session, id:int):
    _class = get_class_by_id(db=db,id=id)

    if _class is None:
        raise Exception(f"Class with id {id} not exist")

    db.delete(_class)
    db.commit()
    return _class

def update_class(db:Session, id:int, name:str, teacher_id:int):
    _class = get_class_by_id(db=db, id=id)

    if _class is None:
        raise Exception(f"Class with id {id} not exist")

    _class.name = name
    _class.teacher_id = teacher_id
    db.commit()
    db.refresh(_class)
    return _class