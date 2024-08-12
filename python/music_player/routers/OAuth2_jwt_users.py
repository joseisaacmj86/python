# Users API con autorización OAuth2 JWT ###

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta # se usan para calcular el tiempo de duracion del token
from app.schemas import User, UserPass
from app import models
from sqlalchemy.orm import Session
from app.database import SessionLocal

ALGORITHM = "HS256" # algoritmo de incriptacion
ACCESS_TOKEN_DURATION = 5 # 1 minute

# generado desde la terminal con (openssl rand -hex 32)
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"

router = APIRouter(prefix="/login",
                   tags=["login"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


# oauth2 = OAuth2PasswordBearer(tokenUrl="login"): es nuestro sistema de autenticacion el cual es capaz de capturar el token que proporcionamos en el login, por tanto
# usamos la dependencia (Depends(oauth2)) para traer el token 
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"]) # para definir contexto de incriptacion


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def search_user(username: str, db: Session):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**db_user.__dict__) # db_user.__dict__: convierte db_user en un diccionario


async def auth_user(token: str = Depends(oauth2), db: Session = Depends(get_db)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username, db)


async def current_user(user: User = Depends(auth_user)):
    if not user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user



@router.post("/")
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.username == form.username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
   
    # user = db.query(models.User).filter(models.User.username == form.username).first()

    if not crypt.verify(form.password, user.password): # A verify le pasamos el password que viene en el formulario (contraseña original) para que verifique con el password encriptado en db
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    # json access_token
    access_token = {
                    "sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION) # calcula el tiempo de expiracion
                   } 

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer", "token": Depends(oauth2)}




@router.get("/me")
async def me(user: User = Depends(current_user)):
    return user