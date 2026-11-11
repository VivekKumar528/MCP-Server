import asyncio

from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

async def create_task_using_mcp():
  async with client:
    result = await client.call_tool(
      "create_task",
      {
        "title":"task2",
        "priority":"high",
        "description":"this is the test from our client"
      }
    )

    print(result.data)
  return result.data


if __name__ == "__main__":
  asyncio.run(create_task_using_mcp())