@app.get("/projects")
def get_projects():
    return [
        {
            "id": 1,
            "title": "WorkforceConnect",
            "desc": "Full-stack application integrating React UI with Python (FastAPI) backend APIs. Demonstrates real-time data retrieval, API integration, and deployment using Render and Netlify."
        },
        {
            "id": 2,
            "title": "Badge Swipes",
            "desc": "End-to-end data pipeline example showing how backend services process and expose data via APIs, and how frontend applications consume and display that data dynamically."
        },
        {
            "id": 3,
            "title": "Orbit Platform",
            "desc": "Represents enterprise-scale system thinking — integrating multiple data sources, APIs, and frontend layers to provide actionable insights in a scalable architecture."
        }
    ]