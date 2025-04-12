from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import db

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Welcome to the ToDo!"}

@app.get('/todos')
async def get_todos(number: Optional[int] = None):
    todos = []
    async for document in db.todos.find():
        document.pop('_id')
        todos.append(document)
    return todos[:number]

@app.get('/todos/{todo_id}')
async def get_todo(todo_id: int):
    todo = await db.todos.find_one({"id": todo_id})
    if todo:
        todo.pop('_id')
        return todo
    else:
        return {"error": "Todo not found"}
    
class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.post('/todos')
async def create_todo(todo: Todo):
    todo_dict = todo.model_dump()
    max_id_todo = await db.todos.find_one(sort=[("id", -1)])
    todo_dict['id'] = (max_id_todo['id'] + 1) if max_id_todo else 1
    await db.todos.insert_one(todo_dict)
    todo_dict.pop('_id')
    return todo_dict

@app.put('/todos/{todo_id}')
async def update_todo(todo_id: int, todo: Todo):
    todo_dict = todo.model_dump()
    result = await db.todos.update_one({"id": todo_id}, {"$set": todo_dict})
    if result.modified_count == 1:
        return {"message": "Todo updated successfully"}
    else:
        return {"error": "Todo not found"}
    
@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id: int):
    result = await db.todos.delete_one({"id": todo_id})
    if result.deleted_count == 1:
        return {"message": "Todo deleted successfully"}
    else:
        return {"error": "Todo not found"}
