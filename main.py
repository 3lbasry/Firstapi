#import FastAPI and datetime modules
from fastapi import FastAPI
from datetime import datetime

#create an instance of FastAPI
app = FastAPI()

#define a root endpoint that returns a simple message
@app.get("/")
def get_root():
    return {"msg": "hi elbasry api"}

#define an about endpoint that returns information about the API
@app.get("/about")
def get_about():
    return {"msg": "This is my first FastAPI project, I am learning FastAPI and building a simple API.  I am excited to learn more about FastAPI and its features."}

#define a health endpoint that returns the status of the API
@app.get("/health") 
def get_health(): 
    return {
            "status": "healthy",
              "version": "1.0.0",
             "msg": "API is running smoothly",
             "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
             }

#define a user endpoint that returns a personalized message for the given username (Path Parameter)
@app.get("/users/{username}")
def get_user(username: str):
    return {"username": username,
            "msg": f"Hello, {username}! Welcome to my FastAPI project."}

#define a query endpoint that returns a personalized message for the given name (Query Parameter)
@app.get("/products")
def get_product(category: str | None = None):
    return {"field": category,
            "msg": f"Here are the products in the {category} field."}

#define a query endpoint for search  (Query Parameter)
@app.get("/search")
def search(q: str | None = None):
    return {"query": q,
            "msg": f"Searching for {q} in the database."}

