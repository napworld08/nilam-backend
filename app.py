@app.get("/projects")
def get_projects():
    return [
        
 {
            "id": 1,
            "title": "Nilam Portfolio Platform",
            "desc": "End-to-end full-stack application demonstrating React frontend, Python backend, API integration, and cloud deployment",
            "details": """
• Frontend: React (state management, event handling, dynamic rendering)
• Backend: Python FastAPI service deployed on cloud
• API: REST endpoints for project data and system health checks
• Integration: Frontend communicates with backend via async API calls
• DevOps: Git-based version control and deployment pipeline (Render)
• Architecture: Decoupled frontend/backend (API-first design)
• Monitoring: Live backend status + response time tracking
• UX: Interactive UI with filtering, search, and expandable components
• CI/CD: Automated deployment via Git push to production
"""
        },
	{
            "id": 2,
            "title": "WorkforceConnect",
            "desc": "Full-stack application integrating React UI with Python (FastAPI) backend APIs. Demonstrates real-time data retrieval, API integration, and deployment using Render and Netlify."
        },
        {
            "id": 3,
            "title": "Badge Swipes",
            "desc": "End-to-end data pipeline example showing how backend services process and expose data via APIs, and how frontend applications consume and display that data dynamically."
        },
        {
            "id": 4,
            "title": "Orbit Platform",
            "desc": "Represents enterprise-scale system thinking — integrating multiple data sources, APIs, and frontend layers to provide actionable insights in a scalable architecture."
        }
    ]