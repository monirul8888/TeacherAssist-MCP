from fastapi import FastAPI

app = FastAPI(
    title="Teacher Assistant MCP Server",
    description="MCP backend for grading, GPA calculation, and report generation",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Teacher Assistant MCP Server is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }