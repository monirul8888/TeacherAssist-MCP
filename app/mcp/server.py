from fastmcp import FastMCP
from app.mcp.tools.student_tools import (
    create_student_tool,
    get_students_tool
)

mcp = FastMCP("TeacherAssist-MCP")


@mcp.tool()
def create_student(student_id: int, name: str):
    return create_student_tool(student_id, name)


@mcp.tool()
def get_students():
    return get_students_tool()


if __name__ == "__main__":
    mcp.run()