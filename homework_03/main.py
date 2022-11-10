from fastapi import FastAPI
from views.view import router as massage_router

app = FastAPI()
app.include_router(massage_router)


@app.get("/")
def read_root():
    return {"Hello": "Suren :-)) !!"}


@app.get("/test")
def read_root1():
    return {"Hello": "World"}


