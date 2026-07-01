from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "hi elbasry api"}

@app.get("/about")
def about():
    return {"msg": "This is my first FastAPI project, I am learning FastAPI and building a simple API.  I am excited to learn more about FastAPI and its features."}

@app.get("/health") 
def health(): 
    return {
            "status": "healthy",
              "version": "1.0.0",
             "msg": "API is running smoothly",
             "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
             }