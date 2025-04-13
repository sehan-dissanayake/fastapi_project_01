from fastapi import APIRouter, HTTPException
from typing import Optional
from models.todo_model import Todo
from controllers import todo_controller

router = APIRouter()

@router.get('/')
async def index():
    return {"message": "Welcome to the ToDo!"}

@router.get('/todos')
async def get_todos(number: Optional[int] = None):
    todos = await todo_controller.get_all_todos()
    return todos[:number]

@router.get('/todos/{todo_id}')
async def get_todo(todo_id: int):
    todo = await todo_controller.get_todo_by_id(todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post('/todos')
async def create_todo(todo: Todo):
    return await todo_controller.create_todo(todo.model_dump())

@router.put('/todos/{todo_id}')
async def update_todo(todo_id: int, todo: Todo):
    updated_count = await todo_controller.update_todo(todo_id, todo.model_dump())
    if updated_count == 1:
        return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete('/todos/{todo_id}')
async def delete_todo(todo_id: int):
    deleted_count = await todo_controller.delete_todo(todo_id)
    if deleted_count == 1:
        return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")