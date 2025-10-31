from fastapi import APIRouter
from models.Task import Task as TaskModel

route = APIRouter(prefix="/api/v1", tags=["Task"])

@route.post("/create")
def createTask(data:TaskModel ):
    return data

@route.get("/seealltasks")
def seeAllTasks():
    return{
        "details":["Data1","Data2"]
    }