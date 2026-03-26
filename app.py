from fastapi import FastAPI

app = FastAPI()

projects = [
    {
        "id": 1,
        "title": "Nilam Portfolio Platform",
        "desc": "End-to-end full-stack application demonstrating React frontend, Python backend, API integration, and cloud deployment",
        "details": "React frontend, FastAPI backend, API integration, deployed on Render"
    },
    {
        "id": 2,
        "title": "WorkforceConnect",
        "desc": "React + FastAPI integration example"
    },
    {
        "id": 3,
        "title": "Badge Swipes",
        "desc": "Data pipeline + API processing example"
    },
    {
        "id": 4,
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