from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def qaytar():
    return {"habar": "Hello World"}

