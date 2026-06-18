from pydantic import BaseModel
from typing import List


class ResultItem(BaseModel):
    subject: str
    exam: str
    marks: float
    grade: str


class ReportResponse(BaseModel):
    student_id: int
    student_name: str
    department: str
    batch: str
    results: List[ResultItem]