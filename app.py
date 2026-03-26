from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

projects = [
    {"id": 1, "title": "WorkforceConnect", "desc": "Employee workforce data"},
    {"id": 2, "title": "Badge Swipes", "desc": "Attendance analytics"},
    {"id": 3, "title": "Orbit Platform", "desc": "R&D data platform"}
]

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.get("/projects")
def get_projects():
    return projects