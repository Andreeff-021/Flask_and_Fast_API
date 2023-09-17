from typing import Annotated
import uvicorn
from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

    def __str__(self):
        return f'Имя: {self.username}, email: {self.email}'


users = []


@app.post("/login")
async def create_user(username: Annotated[str, Form()],
                      email: Annotated[str, Form()],
                      password: Annotated[str, Form()]):
    user = User(id=len(users) + 1, username=username, email=email, password=password)
    users.append(user)
    return 'Пользователь добавлен!'


@app.get("/login", response_class=HTMLResponse)
async def get_new_user(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/update")
async def update_user(user_id: Annotated[int, Form()],
                      username: Annotated[str, Form()],
                      email: Annotated[str, Form()],
                      password: Annotated[str, Form()]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.email = email
            user.password = password
    return 'Данные пользователя обновлены!'


@app.get("/update", response_class=HTMLResponse)
async def get_update_user(request: Request):
    return templates.TemplateResponse("update.html", {"request": request})


@app.post("/delete")
async def delete_user(user_id: Annotated[int, Form()]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
    return 'Пользователь удалён!'


@app.get("/delete", response_class=HTMLResponse)
async def get_delete_user(request: Request):
    return templates.TemplateResponse("delete.html", {"request": request})


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


if __name__ == '__main__':
    uvicorn.run("task:app", host="127.0.0.1", port=8080)
