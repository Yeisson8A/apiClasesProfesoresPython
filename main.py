from fastapi import FastAPI
import uvicorn
import models.models as model
from db.config import engine
from routes.routes_teacher import router as router_teacher
from routes.routes_class import router as router_class

model.Base.metadata.create_all(engine)

app = FastAPI(
    title="Classes and Teachers API",
    description="Operaciones CRUD usando una API",
    version="1.0.0"
)

app.include_router(router=router_teacher,tags=["Teacher"],prefix="/teacher")
app.include_router(router=router_class,tags=["Class"],prefix="/class")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)