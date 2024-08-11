from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
import app.models as models
from app.schemas import Cancion, CancionCreate

router = APIRouter(prefix="/songs",
                   tags=["songs"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Cancion, status_code=status.HTTP_201_CREATED)
async def create_cancion(cancion: CancionCreate, db: Session = Depends(get_db)):
    db_cancion = models.Song(**cancion.dict())
    db.add(db_cancion)
    db.commit()
    db.refresh(db_cancion)
    return db_cancion

@router.get("/", response_model=List[Cancion], status_code=status.HTTP_200_OK)
async def get_canciones(db: Session = Depends(get_db)):
    return db.query(models.Song).all()

@router.get("/{song_id}", response_model=Cancion, status_code=status.HTTP_200_OK)
async def get_cancion(song_id: int, db: Session = Depends(get_db)):
    cancion = db.query(models.Song).filter(models.Song.song_id == song_id).first()
    if cancion is None:
        raise HTTPException(status_code=404, detail="Cancion not found")
    return cancion

@router.delete("/{song_id}", status_code=status.HTTP_200_OK)
async def delete_cancion(song_id: int, db: Session = Depends(get_db)):
    cancion = db.query(models.Song).filter(models.Song.song_id == song_id).first()
    if cancion is None:
        raise HTTPException(status_code=404, detail="Cancion not found")
    db.delete(cancion)
    db.commit()
    return {"detail": "Cancion deleted successfully"}

@router.put("/{song_id}", response_model=Cancion, status_code=status.HTTP_200_OK)
async def update_cancion(song_id: int, cancion: CancionCreate, db: Session = Depends(get_db)):
    db_cancion = db.query(models.Song).filter(models.Song.song_id == song_id).first()
    if db_cancion is None:
        raise HTTPException(status_code=404, detail="Cancion not found")
    for key, value in cancion.dict().items():
        setattr(db_cancion, key, value)
    db.commit()
    db.refresh(db_cancion)
    return db_cancion
