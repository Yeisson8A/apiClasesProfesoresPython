from typing import Optional, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")

class TeacherSchema(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=255, min_length=1)
    
    class Config:
        orm_mode = True
        schema_extra  = {
            "example":
                {
                    "id": 0,
                    "name": "name teacher"
                }
        }

class ClassSchema(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=255, min_length=1)
    teacher_id: Optional[int] = None
    
    class Config:
        orm_mode = True
        schema_extra  = {
            "example":
                {
                    "id": 0,
                    "name": "class name",
                    "teacher_id": 0
                }
        }

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]