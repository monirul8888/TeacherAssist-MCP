import os

from app.services.report_service import get_student_report
from app.services.pdf_service import generate_pdf


def generate_student_pdf(db, student_id: int):

    report = get_student_report(db, student_id)

    if not report:
        return None

    os.makedirs("reports", exist_ok=True)

    file_path = f"reports/student_{student_id}.pdf"

    generate_pdf(report, file_path)

    return file_path