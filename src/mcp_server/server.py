from typing import Literal
from uuid import uuid4

from fastmcp import FastMCP
from mcp_server.database import (
  get_all_tasks,
  save_task,
  update_task_status_in_db
)

mcp = FastMCP("First MCP SERVER")

@mcp.tool(name="create_task", description="this tool is created to create new tasks")
def create_task(title:str, priority:str, description:str="") -> dict:
  """
  this function creates new tasks in our database
  """
  task_id = str(uuid4())
  status = "to do"

  task = {"task_id":task_id, "title":title, "description":description, "status" : status, "priority":priority}

  save_task(task)

  return task

if __name__ == "__main__":
  mcp.run(transport="http", port=8000)
  # create_task(title="this is second task", description="this is a test task")

# @mcp.tool(name="list_tasks", description="this tool provide all the list of tasks in our database")
