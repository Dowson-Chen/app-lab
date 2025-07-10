from fastapi import FastAPI
from common.utils import greet

app = FastAPI()

@app.get('/')
def root():
    return {'message': greet('from TODO app')}
