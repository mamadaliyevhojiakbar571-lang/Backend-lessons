from fastapi import FastAPI, HTTPException

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

@app.get("/tasks/{task_id}")
def task(task_id: int):
    if task_id < 0 or task_id >= len(vazifalar):
        raise HTTPException(status_code=404, detail="Vazifa topilmadi")
    return {"vazifa": vazifalar[task_id]}

@app.get("/users/{user_id}")
def user(user_id: int):
    if user_id < 0 or user_id >= len(foydalanuvchilar):
        raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")
    return {"foydalanuvchi": foydalanuvchilar[user_id]}

