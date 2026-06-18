from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.mark import Mark


def get_student_report(db: Session, student_id: int):

    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if not student:
        return None

    marks = db.query(Mark).filter(
        Mark.student_id == student_id
    ).all()

    results = []

    for m in marks:
        results.append({
            "subject": m.subject.subject_name,
            "exam": m.exam.exam_name,
            "marks": m.marks_obtained,
            "grade": m.grade
        })

    return {
        "student_id": student.student_id,
        "student_name": student.name,
        "department": student.department,
        "batch": student.batch,
        "results": results
    }