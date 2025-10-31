from fastapi import FastAPI
from routes.Task import route as TaskRoute
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Task Manager APIS - Sachin Sharma", version="0.0.1")

# Optional: Allow frontend (React) access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(TaskRoute)

@app.get("/")
def initial():
    return{
        "message":"Hi sachin"
        }