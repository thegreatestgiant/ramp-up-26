from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def hello_world(): 
    return {"Message":"Hello There"}
