from pydantic import BaseModel


class StudentCreate(BaseModel):
    student_id: int
    name: str


class StudentResponse(BaseModel):
    student_id: int
    name: str

    class Config:
        from_attributes = True