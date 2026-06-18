from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.mark import MarkCreate, MarkResponse
from app.services.mark import (
    create_mark,
    get_marks,
    get_marks_by_student
)

router = APIRouter(prefix="/marks", tags=["Marks"])


# CREATE MARK
@router.post("/", response_model=MarkResponse)
def add_mark(
    mark: MarkCreate,
    db: Session = Depends(get_db)
):
    return create_mark(db, mark)


# GET ALL MARKS (with student + subject + exam info)
@router.get("/", response_model=List[MarkResponse])
def list_marks(db: Session = Depends(get_db)):
    return get_marks(db)


# GET MARKS BY STUDENT
@router.get("/student/{student_id}", response_model=List[MarkResponse])
def marks_by_student(student_id: int, db: Session = Depends(get_db)):
    return get_marks_by_student(db, student_id)