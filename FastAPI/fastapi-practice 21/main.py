from os import name
from fastapi import responses
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse
from exceptions import StoryException
from fastapi import FastAPI
from router import blog_get, blog_post, user, article, product, file
from auth import authentication
from templates import templates
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time

app = FastAPI()
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
  return JSONResponse(
    status_code=418,
    content={'detail': exc.name}
  )

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#   return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)


@app.middleware("http")
async def add_middleware(request: Request, call_next):
  start_time = time.time()
  response = await call_next(request)
  duration = time.time() - start_time
  response.headers['duration'] = str(duration)
  return response


origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)

app.mount('/files', StaticFiles(directory="files"), name='files')
app.mount('/templates/static', 
      StaticFiles(directory="templates/static"),
      name="static"
)