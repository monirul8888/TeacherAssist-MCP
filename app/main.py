from fastapi import FastAPI

from app.db.database import engine, Base

from app.routes.student import router as student_router
from app.routes.subject import router as subject_router

from app.routes.exam import router as exam_router
from app.routes.mark import router as mark_router
from app.routes.report import router as report_router


# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Teacher Assistant MCP Server",
    description="MCP backend for grading, GPA calculation, and report generation",
    version="1.0.0",
)

# routers
app.include_router(student_router, prefix="/students", tags=["Students"])

app.include_router(subject_router, prefix="/subjects", 
                   tags=["Subjects"])

app.include_router(exam_router, prefix="/exams", tags=["Exams"])

app.include_router(mark_router)
app.include_router(report_router)



@app.get("/")
def root():
    return {"message": "Teacher Assistant MCP Server is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}