from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.report_pipeline import generate_student_pdf

router = APIRouter(prefix="/report", tags=["Report"])


@router.get("/pdf/{student_id}")
def create_report(student_id: int, db: Session = Depends(get_db)):

    file_path = generate_student_pdf(db, student_id)

    if not file_path:
        raise HTTPException(status_code=404, detail="Student not found")

    return {
        "message": "PDF generated",
        "file": file_path
    }