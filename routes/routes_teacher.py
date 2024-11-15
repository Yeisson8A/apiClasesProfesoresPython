from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from db import crud_teacher
from db.config import get_db
from schemas.schemas import Response, TeacherSchema
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_teacher_service(request: TeacherSchema, db: Session = Depends(get_db)):
    crud_teacher.create_teacher(db, teacher=request)
    return Response(status="Ok", code="201", message="Teacher created successfully",result=jsonable_encoder(request)).model_dump(exclude_none=True)

@router.get("/")
async def get_teachers(db: Session = Depends(get_db)):
    _teachers = crud_teacher.get_teachers(db)
    return Response(status="Ok", code="200", message="Success fetch all data", result=jsonable_encoder(_teachers))

@router.get("/{id}")
async def get_teacher_by_id(id: int, db: Session = Depends(get_db)):
    _teacher = crud_teacher.get_teacher_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=jsonable_encoder(_teacher))

@router.get("/{id}/allclasses")
async def get_teacher_by_id_with_classes(id: int, db: Session = Depends(get_db)):
    _teacher_with_classes = crud_teacher.get_teacher_by_id_with_classes(db, id=id)
    return Response(status="Ok", code="200", 
                    message="Success fetch data", 
                    result={
                        "id": _teacher_with_classes.id,
                        "name": _teacher_with_classes.name,
                        "classes": [{"id": cls.id, "name": cls.name} for cls in _teacher_with_classes.classes]
                    })

@router.put("/{id}")
async def update_teacher(id: int, request: TeacherSchema, db: Session = Depends(get_db)):
    try:
        _teacher = crud_teacher.update_teacher(db, id=id, name=request.name)
        return Response(status="Ok", code="200", message="Teacher updated successfully", result=jsonable_encoder(_teacher))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}")
async def delete_teacher(id: int, db: Session = Depends(get_db)):
    try:
        _teacher = crud_teacher.remove_teacher(db, id=id)
        return Response(status="Ok", code="200", message="Teacher deleted successfully", result=None).model_dump(exclude_none=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))