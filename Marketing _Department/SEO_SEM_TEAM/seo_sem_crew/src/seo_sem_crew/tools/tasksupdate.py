from crewai.tools import BaseTool
from typing import Type, Literal
from pydantic import BaseModel, Field

class TaskStatusUpdateSchema(BaseModel):
    task_name: str = Field(..., description="The name of the task being updated.")
    status: Literal["COMPLETED", "PENDING"] = Field(..., description="Task status must be 'COMPLETED' or 'PENDING'.")
    chat_message_id: int = Field(..., description="The ID of the chat message associated with the task.")

class TaskStatusUpdate(BaseTool):
    name: str = "task_status_update"
    description: str = "Updates the task status dynamically to either 'COMPLETED' or 'PENDING' along with the task name and chat message ID."
    args_schema: Type[BaseModel] = TaskStatusUpdateSchema  # Ensure correct argument validation

    def _run(self, task_name: str, status: str, chat_message_id: int) -> str:
        """
        Updates the task status of the given task_name associated with the chat_message_id.

        Args:
            task_name (str): The name of the task being updated.
            status (str): Must be 'COMPLETED' or 'PENDING'.
            chat_message_id (int): The ID of the chat message associated with the task.

        Returns:
            str: A message confirming the update.
        """

        # Print and return the result
        print(f"Updated Task: {task_name} | Status: {status} | Chat Message ID: {chat_message_id}")
        return f"Task '{task_name}' status updated successfully to {status} for Chat Message ID {chat_message_id}"