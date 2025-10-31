from fastapi import APIRouter
from models.Task import Task as TaskModel
from models.Task import EnterName as NameModel



route = APIRouter(prefix="/api/v1", tags=["Task"])

@route.post("/create")
def createTask(data:TaskModel ):
    return data

@route.post("/createstudent")
def createStudent(data: NameModel):
    return data