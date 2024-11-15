from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from db import crud_class
from db.config import get_db
from schemas.schemas import Response, ClassSchema
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
async def create_class_service(request: ClassSchema, db: Session = Depends(get_db)):
    try:
        crud_class.create_class(db, cl=request)
        return Response(status="Ok", code="201", message="Class created successfully",result=jsonable_encoder(request)).model_dump(exclude_none=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def get_classes(db: Session = Depends(get_db)):
    _classes = crud_class.get_classes(db)
    return Response(status="Ok", code="200", message="Success fetch all data", result=jsonable_encoder(_classes))

@router.get("/{id}")
async def get_class_by_id(id: int, db: Session = Depends(get_db)):
    _class = crud_class.get_class_by_id(db, id=id)
    return Response(status="Ok", code="200", message="Success fetch data", result=jsonable_encoder(_class))

@router.put("/{id}")
async def update_class(id: int, request: ClassSchema, db: Session = Depends(get_db)):
    try:
        _class = crud_class.update_class(db, id=id, name=request.name, teacher_id=request.teacher_id)
        return Response(status="Ok", code="200", message="Class updated successfully", result=jsonable_encoder(_class))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id}")
async def delete_class(id: int, db: Session = Depends(get_db)):
    try:
        _class = crud_class.remove_class(db, id=id)
        return Response(status="Ok", code="200", message="Class deleted successfully", result=None).model_dump(exclude_none=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))