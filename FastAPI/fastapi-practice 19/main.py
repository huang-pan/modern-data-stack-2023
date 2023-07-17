from fastapi import FastAPI


app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello world!'}