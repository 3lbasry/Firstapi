from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"msg": "hi elbasry api"}

@app.get("/about")
def about():
    return {"msg": "This is my first FastAPI project, I am learning FastAPI and building a simple API.  I am excited to learn more about FastAPI and its features."}

