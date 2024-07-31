from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"], # tags nos ayuda a agrupar y organizar las rutas de products en la documentacion
                   responses={404: {"message": "No encontrado"}})

# Inicia el server: uvicorn api_user:router --reload

# BeseModel: nos da la capacidad de crear una identidad

# entidad user

class User(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    url: str
    age: int
    
users_list = [User(id=1, name="jose", last_name="alvarez", email="jose@example.com", url="http://example.com", age="37"),
              User(id=2, name= "edwar", last_name="soto", email= "soto@example.com", url= "http://example.com", age="22"),
              User(id=3, name="pedro", last_name="villa", email="villa@example.com", url="http://example.com", age="31")]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "jose", "last_name":"alvarez", "email": "jose@example.com", "url": "http://example.com", "age": "37"},
            {"name": "edwar", "last_name":"soto", "email": "soto@example.com", "url": "http://example.com", "age": "22"},
            {"name": "pedro", "last_name":"villa", "email": "villa@example.com", "url": "http://example.com", "age": "31"}]



@router.get("/")
async def users():
    return  users_list

    
# Parametro por path: http://127.0.0.1:8000/user/4
@router.get("/{id}")
async def user(id:int):
    return search_user(id)
    
    
# Parametro por query: http://127.0.0.1:8000/userquery/?id=1
@router.get("/userquery/")
async def user(id:int):
    return search_user(id)

#2 o mas parametros por query: http://127.0.0.1:8000/userquery/?id=1&name=jose
@router.get("/userquery/")
async def user(id:int, name:str):
    return search_user(id, name)


# status_code: modifica el codigo error por defecto, el cual es el 200. Esto lo podemos hacer si necesitamos
# personalizar el codigo de salida para que vaya mas acorde a la respuesta que estoy recibiendo.
"""
@router.post("/userquery/", status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
        return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)
        return user
"""

@router.post("/userquery/", status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
        # HTTPException(403, "|User not found")
        raise HTTPException(status_code=404, detail= "el usuario ya existe")
 
    users_list.append(user)
    return user      
        
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user
    
    
    
@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}
    

    
    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return  list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
    
    
