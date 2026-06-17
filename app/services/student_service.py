from sqlalchemy.orm import Session
from app.models.student import Student


def create_student(db: Session, student_id: int, name: str):
    student = Student(student_id=student_id, name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_students(db: Session):
    return db.query(Student).all()