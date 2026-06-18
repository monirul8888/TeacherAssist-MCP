from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generate_pdf(report: dict, file_path: str):

    c = canvas.Canvas(file_path, pagesize=A4)

    y = 800

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Student Report")

    y -= 40

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"ID: {report['student_id']}")
    y -= 20
    c.drawString(50, y, f"Name: {report['student_name']}")
    y -= 20
    c.drawString(50, y, f"Department: {report['department']}")
    y -= 20
    c.drawString(50, y, f"Batch: {report['batch']}")

    y -= 40

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Results:")

    y -= 20

    c.setFont("Helvetica", 11)

    for r in report["results"]:
        text = f"{r['subject']} | {r['exam']} | {r['marks']} | {r['grade']}"
        c.drawString(50, y, text)
        y -= 20

    c.save()

    return file_path