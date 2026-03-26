from fastapi import FastAPI

app = FastAPI()

projects = [
    {
        "id": 1,
        "title": "Nilam Portfolio Platform",
        "desc": "End-to-end full-stack application demonstrating React frontend, Python backend, API integration, and cloud deployment",
    },
    {
        "id": 2,
        "title": "WorkforceConnect",
        "desc": "React + FastAPI integration example"
    },
    {
        "id": 3,
        "title": "Orbit Platform",
        "desc": "Enterprise data integration system"
    }
]

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/projects")
def get_projects():
    return projects