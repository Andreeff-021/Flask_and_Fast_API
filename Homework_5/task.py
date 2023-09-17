from typing import Annotated
import uvicorn
from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str


users = []


@app.post("/login")
async def create_user(username: Annotated[str, Form()],
                      email: Annotated[str, Form()],
                      password: Annotated[str, Form()]):
    user = User(id=len(users) + 1, username=username, email=email, password=password)
    users.append(user)


@app.get("/login", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run("task:app", host="127.0.0.1", port=8080)
