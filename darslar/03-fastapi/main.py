from fastapi import FastAPI

vazifalar = ["Kitob o'qish", "Ish qilish"]
foydalanuvchilar = ["Sardor", "Akmal", "Jasur"]

app = FastAPI()
@app.get("/")
def qaytar():
    return {"habar": "Hello World"}

@app.get("/tasks")
def tasks():
    return {"vazifalar": vazifalar}

@app.get("/users")
def users():
    return {"foydalanuvchilar": foydalanuvchilar }
