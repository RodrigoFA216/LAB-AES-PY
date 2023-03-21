from fastapi import FastAPI
from app.routes.router import router


app = FastAPI()
app.include_router(router)


@app.get('/', tags=['Testing'])
def root():
    return 'ok'
