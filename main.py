from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Go shopping'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'Study for exam'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': 'Meditate 20 minutes'}
]

@app.get('/')
def index():
    return {'message': 'Welcome to the ToDo'}

@app.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return todo
    return {'message': 'Todo not found'}
          
@app.get('/todos')
def get_todos(first_n: int = None):
    if first_n is not None:
        return all_todos[:first_n]
    return all_todos

class Todo(BaseModel):
    todo_id: int
    todo_name: str
    todo_description: Optional[str] = None

@app.post('/todos')
def create_todo(request: Todo):
    new_todo = request.model_dump()
    all_todos.append(new_todo)
    return {'message': 'Todo created', 'todo': new_todo}
 