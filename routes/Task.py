from fastapi import APIRouter

route = APIRouter(prefix="/api/v1")

@route.get("/create")
def createTask():
    return{
        "msg":"Task Created successfully"
    }

@route.get("/seealltasks")
def seeAllTasks():
    return{
        "details":["Data1","Data2"]
    }