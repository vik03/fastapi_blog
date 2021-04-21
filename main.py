from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'vikram'}}


@app.get('/about')
def about():
    return {'data': 'about page'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


# @app.get('/blog/{id}/comments')
# def show_comments(id):
#     return {'data': {'1', '2'}}


# @app.get('/blog?limit=10&published=true')
# http://127.0.0.1:8000/blog?limit=50&published=true&sort=latest
@app.get('/blog')
def show_with_params(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from database'}
    else:
        return {'data': 'all published blogs'}


@app.get('/blog/{id}/comments')
def show_limits(id: int, limit=10):
    if id > 20:
        return {'data': 'limit should not exceed above 20 for performance reasons'}
    else:
        lst = []
        for i in range(1, id+1):
            lst.append(i)
        return {'data': lst}




# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=9000)