# Users DB API

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId  # se importa para poder hacer busquedas por id ya que mongo los genera como un ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())


@router.get("/{id}")  # Path
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.get("/")  # Query
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user) # transforma el modelo usuario en un diccionario, ya que un json es un diccionario en python
    
    #por defecto, mongodb cada vez que inserto un registro le da un id unico. Los id son de tipo string en mongo por defecto ya que asi puede crear ids unicos mucho mas largos
    del user_dict["id"] # por tanto, eliminamos el campo id para un registro nuevo para que mongo lo autogenere
        
    id = db_client.users.insert_one(user_dict).inserted_id #insert_one: para insertar un registro

    # el nombre de la clave unica que crea mongo por registro es "_id" y no "id"
    new_user = user_schema(db_client.users.find_one({"_id": id})) # find_one: para buscar un registro y por defecto retorna un json

    return User(**new_user)


@router.put("/", response_model=User)
async def user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id", ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario"}



# Helper

def search_user(field: str, key):

    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}
