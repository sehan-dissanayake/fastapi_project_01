from database import db

async def get_all_todos():
    todos = []
    async for document in db.todos.find():
        document.pop('_id')
        todos.append(document)
    return todos

async def get_todo_by_id(todo_id: int):
    todo = await db.todos.find_one({"id": todo_id})
    if todo:
        todo.pop('_id')
    return todo

async def create_todo(todo_dict: dict):
    max_id_todo = await db.todos.find_one(sort=[("id", -1)])
    todo_dict['id'] = (max_id_todo['id'] + 1) if max_id_todo else 1
    await db.todos.insert_one(todo_dict)
    todo_dict.pop('_id')
    return todo_dict

async def update_todo(todo_id: int, todo_dict: dict):
    result = await db.todos.update_one({"id": todo_id}, {"$set": todo_dict})
    return result.modified_count

async def delete_todo(todo_id: int):
    result = await db.todos.delete_one({"id": todo_id})
    return result.deleted_count