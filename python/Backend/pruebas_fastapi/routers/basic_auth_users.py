# Users API con autorización OAuth2 básica

from fastapi import APIRouter, Depends, HTTPException, status
#from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


# OAuth2PasswordBearer: nos autentica nuestro usuario y contraseña
# OAuth2PasswordRequestForm: es la forma como se va a enviar desde el cliente a nuestro backend los criterior de autenticacion y la foma como nuestro backend los recive


router = APIRouter(prefix="/basicauth",
                   tags=["basicauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# app=FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "joseisaac": {
        "username": "joseisaac",
        "full_name": "jose isaac",
        "email": "joseisaac@example.com",
        "disabled": False,
        "password": "123456789"
    },
    "joseisaac2": {
        "username": "joseisaac2",
        "full_name": "jose isaac 2",
        "email": "joseisaac2@example.com",
        "disabled": True,
        "password": "987654321"
    }
}

# **: para indicar que va un numero arbitrarios de parametros
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username]) # **: 

# oauth2 = OAuth2PasswordBearer(tokenUrl="login"): es nuestro sistema de autenticacion el cual es capaz de capturar el token que proporcionamos en el login, por tanto
# usamos la dependencia (Depends(oauth2)) para traer el token 
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user


# Depends(): ayuda a que la operacion reciba datos pero que no dependa de nadies. El Depends es un tema que tiene que ver con la autorizacion.
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}

# Aqui aplicamos el criterio de dependencia para implementar operaciones sin necesidad de estar autenticandonos todo el tiempo 
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
