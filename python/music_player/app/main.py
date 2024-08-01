
# uvicorn app.main:app --reload

from fastapi import FastAPI
from app.database import engine
import app.models as models
from routers import registros
from routers import registros, artists, albums, songs

# Crea todas las tablas en la base de datos si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluye los routers
app.include_router(registros.router, prefix="/registers", tags=["registers"])
app.include_router(artists.router)
app.include_router(albums.router)
app.include_router(songs.router)



















"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel # Modelo para pedir dato por post
from typing import Annotated
import app.models as models
from  app.database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

class IngresoBase(BaseModel):
    documentoingreso: str
    nombrepersona: str
    
class IngresoBase2(BaseModel):
    id: int
    documentoingreso: str
    nombrepersona: str
    
 # funcion para ejecutar la db o cerrar la db   
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/registro/", status_code=status.HTTP_201_CREATED)
async def create_registro(registro: IngresoBase, db: db_dependency):
    db_registro = models.Ingreso(**registro.dict())
    db.add(db_registro)
    db.commit()
    return "El registro se creo exitosamente"

@app.get("/listaregistros/", status_code=status.HTTP_200_OK)
async def get_registros(db: db_dependency):
    registros = db.query(models.Ingreso).all()
    return registros

@app.get("/consultaregistro/{documento_ingreso}", status_code=status.HTTP_200_OK)
async def get_registro_by_documentoingreso(documento_ingreso, db: db_dependency):
    registro = db.query(models.Ingreso).filter(models.Ingreso.documentoingreso==documento_ingreso).first() #para buscar un registro
    if registro is not None:
        HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@app.delete("/eliminaregistro/{id_registro}", status_code=status.HTTP_200_OK)
async def delete_registro_by_id(id_registro, db: db_dependency):
    deleteregistro = db.query(models.Ingreso).filter(models.Ingreso.id==id_registro).first()
    if deleteregistro is not None:
        HTTPException(status_code=404, detail="Registro no encontrado")
    db.delete(deleteregistro)
    db.commit()
    return "Registro eliminado exitosamente"

# con POST se puede actualizar un registro pero el metodo no es idempotente, lo que significa que
# múltiples solicitudes pueden resultar en múltiples recursos creados o modificaciones adicionales.
# Ya que POST usualmente es utilizado para crear recursos.
@app.post("/actualizarregistro/", status_code=status.HTTP_200_OK)
async def update_registro(registro: IngresoBase2, db: db_dependency):
    updateregistro = db.query(models.Ingreso).filter(models.Ingreso.id==registro.id).first()
    if updateregistro is not None:
        HTTPException(status_code=404, detail="Registro no encontrado")
    updateregistro.documentoingreso = registro.documentoingreso
    updateregistro.nombrepersona = registro.nombrepersona
    db.commit()
    return "Registro actualizado exitosamente"


# PUT es usualmente utilizado para actualizar recursos existentes.
# Es idempotente, lo que significa que múltiples solicitudes tienen el mismo efecto que una sola solicitud.
@app.put("/actualizarregistro/", status_code=status.HTTP_200_OK)
async def update_registro(registro: IngresoBase2, db: db_dependency):
    updateregistro = db.query(models.Ingreso).filter(models.Ingreso.id==registro.id).first()
    if updateregistro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    updateregistro.documentoingreso = registro.documentoingreso
    updateregistro.nombrepersona = registro.nombrepersona
    db.commit()
    return "Registro actualizado exitosamente"

"""




"""
from fastapi import FastAPI
from .routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
"""