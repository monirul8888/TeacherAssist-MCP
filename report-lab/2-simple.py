
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)

# =====================================================
# DOCUMENT SETUP
# =====================================================

doc = SimpleDocTemplate(
    "report.pdf",
    pagesize=A4,
    leftMargin=40,
    rightMargin=40,
    topMargin=45,
    bottomMargin=45
)

styles = getSampleStyleSheet()

# =====================================================
# COLORS
# =====================================================

PRIMARY = colors.HexColor("#0F4C81")
LIGHT_BLUE = colors.HexColor("#EAF2F8")
LIGHT_GRAY = colors.HexColor("#F8F9FA")
BORDER = colors.HexColor("#B0BEC5")

# =====================================================
# STYLES
# =====================================================

university_style = ParagraphStyle(
    "University",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=20,
    textColor=PRIMARY,
    leading=24
)

report_title_style = ParagraphStyle(
    "ReportTitle",
    parent=styles["Heading1"],
    alignment=TA_CENTER,
    fontSize=13,
    textColor=colors.black,
)

section_style = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontSize=12,
    textColor=PRIMARY,
    spaceBefore=10,
    spaceAfter=8,
)

body_style = styles["BodyText"]

elements = []

# =====================================================
# UNIVERSITY HEADER
# =====================================================

elements.append(
    Paragraph(
        "ABC UNIVERSITY",
        university_style
    )
)

elements.append(
    Paragraph(
        "Office of the Controller of Examinations",
        report_title_style
    )
)

elements.append(
    Paragraph(
        "ACADEMIC PERFORMANCE REPORT",
        report_title_style
    )
)

elements.append(Spacer(1, 8))
elements.append(HRFlowable(width="100%", color=PRIMARY))
elements.append(Spacer(1, 12))

# =====================================================
# REPORT INFORMATION
# =====================================================

report_info = Table(
    [
        ["Academic Session", "Spring 2026"],
        ["Faculty", "Faculty of Engineering"],
        ["Department", "Computer Science & Engineering"],
        ["Program", "B.Sc. in Computer Science & Engineering"]
    ],
    colWidths=[180, 300]
)

report_info.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

elements.append(report_info)

# =====================================================
# STUDENT INFORMATION
# =====================================================

elements.append(
    Paragraph("Student Information", section_style)
)

student_info = Table(
    [
        ["Student Name", "John Doe"],
        ["Student ID", "CSE2026001"],
        ["Batch", "2023"],
        ["Semester", "6th Semester"],
        ["Academic Advisor", "Dr. Sarah Ahmed"]
    ],
    colWidths=[180, 300]
)

student_info.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

elements.append(student_info)

# =====================================================
# SEMESTER RESULTS
# =====================================================

elements.append(
    Paragraph("Semester Results", section_style)
)

course_data = [
    ["Course Code", "Course Title", "Credit", "Marks", "Grade", "Grade Point"],
    ["CSE301", "Data Structures", "3.0", "87", "A+", "4.00"],
    ["CSE302", "Algorithms", "3.0", "90", "A+", "4.00"],
    ["CSE401", "Machine Learning", "3.0", "85", "A+", "4.00"],
    ["CSE402", "Database Systems", "3.0", "88", "A+", "4.00"],
    ["CSE403", "Software Engineering", "3.0", "86", "A+", "4.00"],
]

course_table = Table(
    course_data,
    colWidths=[70, 180, 55, 55, 55, 70]
)

course_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

    ("ROWBACKGROUNDS",
     (0, 1),
     (-1, -1),
     [colors.white, LIGHT_GRAY]),

    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),

    ("ALIGN", (0, 0), (-1, -1), "CENTER"),

    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

    ("PADDING", (0, 0), (-1, -1), 6),
]))

elements.append(course_table)

# =====================================================
# ACADEMIC SUMMARY
# =====================================================

elements.append(
    Paragraph("Academic Summary", section_style)
)

summary_data = [
    ["Semester GPA", "3.95"],
    ["Cumulative GPA (CGPA)", "3.92"],
    ["Credits Registered", "15.00"],
    ["Credits Earned", "15.00"],
    ["Total Credits Earned", "96.00"],
    ["Class Rank", "5 of 120"],
    ["Academic Standing", "Dean's List"],
    ["Scholarship Status", "Merit Scholarship"]
]

summary_table = Table(
    summary_data,
    colWidths=[220, 180]
)

summary_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

elements.append(summary_table)

# =====================================================
# ATTENDANCE
# =====================================================

elements.append(
    Paragraph("Attendance Summary", section_style)
)

attendance = Table(
    [
        ["Theory Courses", "93%"],
        ["Laboratory Courses", "97%"],
        ["Overall Attendance", "95%"]
    ],
    colWidths=[220, 180]
)

attendance.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

elements.append(attendance)

# =====================================================
# ACHIEVEMENTS
# =====================================================

elements.append(
    Paragraph("Academic Achievements", section_style)
)

achievements = Paragraph(
    """
    • Dean's List Recipient (Spring 2026)<br/>
    • Merit Scholarship Awardee<br/>
    • University Programming Contest Finalist<br/>
    • Research Assistant, Artificial Intelligence Lab
    """,
    body_style
)

elements.append(achievements)

# =====================================================
# ADVISOR REMARKS
# =====================================================

elements.append(
    Paragraph("Advisor Remarks", section_style)
)

remarks = Paragraph(
    """
    The student has demonstrated excellent academic performance
    during the semester and has successfully completed all
    registered courses. Performance in core Computer Science
    subjects remains consistently strong. The student is
    recommended for advanced academic and research activities.
    """,
    body_style
)

elements.append(remarks)

# =====================================================
# DEGREE PROGRESS
# =====================================================

elements.append(
    Paragraph("Degree Progress", section_style)
)

degree_progress = Table(
    [
        ["Total Program Credits", "136"],
        ["Credits Completed", "96"],
        ["Credits Remaining", "40"],
        ["Completion Percentage", "70.6%"]
    ],
    colWidths=[220, 180]
)

degree_progress.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

elements.append(degree_progress)

# =====================================================
# FOOTER
# =====================================================

elements.append(Spacer(1, 25))

verification = Table(
    [
        ["Document ID", "APR-2026-001245"],
        ["Issue Date", "18 June 2026"],
        ["Verification Status", "Official Academic Record"]
    ],
    colWidths=[180, 300]
)

verification.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT_BLUE),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
    ("PADDING", (0, 0), (-1, -1), 7),
]))

elements.append(verification)

elements.append(Spacer(1, 40))

signature = Table(
    [[
        "____________________\nAcademic Advisor",
        "____________________\nRegistrar"
    ]],
    colWidths=[240, 240]
)

signature.setStyle(TableStyle([
    ("ALIGN", (0, 0), (-1, -1), "CENTER")
]))

elements.append(signature)

# =====================================================
# BUILD PDF
# =====================================================

doc.build(elements)

print("Academic report generated successfully.")

