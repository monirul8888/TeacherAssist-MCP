from pydantic import BaseModel


# nested schemas
class StudentMini(BaseModel):
    student_id: int
    name: str

    class Config:
        from_attributes = True


class SubjectMini(BaseModel):
    subject_id: int
    subject_name: str

    class Config:
        from_attributes = True


class ExamMini(BaseModel):
    exam_id: int
    exam_name: str

    class Config:
        from_attributes = True


# request schema
class MarkCreate(BaseModel):
    student_id: int
    subject_id: int
    exam_id: int
    marks_obtained: float


# response schema
class MarkResponse(BaseModel):
    id: int
    marks_obtained: float
    grade: str | None = None

    student: StudentMini
    subject: SubjectMini
    exam: ExamMini

    class Config:
        from_attributes = True