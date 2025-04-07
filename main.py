from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data": "Blog list"}

@app.get("/blog/unpublished")
def get_unpublished_blogs():
    return {"data": "Unpublished blogs"}

@app.get("/blog/{id}")
def get_blog(id: int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def get_blog_comments(id: int):
    return {"data": {"id": id, "comments": ["comment1", "comment2"]}}