from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import app.models as models
from app.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

class IngresoBase(BaseModel):
    documentoingreso: str
    nombrepersona: str

class IngresoBase2(BaseModel):
    id: int
    documentoingreso: str
    nombrepersona: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/registro/", status_code=status.HTTP_201_CREATED)
async def create_registro(registro: IngresoBase, db: db_dependency):
    db_registro = models.Ingreso(**registro.dict())
    db.add(db_registro)
    db.commit()
    return "El registro se creó exitosamente"

@router.get("/listaregistros/", status_code=status.HTTP_200_OK)
async def get_registros(db: db_dependency):
    registros = db.query(models.Ingreso).all()
    return registros

@router.get("/consultaregistro/{documento_ingreso}", status_code=status.HTTP_200_OK)
async def get_registro_by_documentoingreso(documento_ingreso: str, db: db_dependency):
    registro = db.query(models.Ingreso).filter(models.Ingreso.documentoingreso == documento_ingreso).first()
    if registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@router.delete("/eliminaregistro/{id_registro}", status_code=status.HTTP_200_OK)
async def delete_registro_by_id(id_registro: int, db: db_dependency):
    deleteregistro = db.query(models.Ingreso).filter(models.Ingreso.id == id_registro).first()
    if deleteregistro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    db.delete(deleteregistro)
    db.commit()
    return "Registro eliminado exitosamente"

@router.post("/actualizarregistro/", status_code=status.HTTP_200_OK)
async def update_registro(registro: IngresoBase2, db: db_dependency):
    updateregistro = db.query(models.Ingreso).filter(models.Ingreso.id == registro.id).first()
    if updateregistro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    updateregistro.documentoingreso = registro.documentoingreso
    updateregistro.nombrepersona = registro.nombrepersona
    db.commit()
    return "Registro actualizado exitosamente"

@router.put("/actualizarregistro/", status_code=status.HTTP_200_OK)
async def update_registro_put(registro: IngresoBase2, db: db_dependency):
    updateregistro = db.query(models.Ingreso).filter(models.Ingreso.id == registro.id).first()
    if updateregistro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    updateregistro.documentoingreso = registro.documentoingreso
    updateregistro.nombrepersona = registro.nombrepersona
    db.commit()
    return "Registro actualizado exitosamente"
