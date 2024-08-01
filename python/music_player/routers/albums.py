from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
import app.models as models
from app.schemas import Album, AlbumCreate

router = APIRouter(prefix="/albums",
                   tags=["albums"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Album, status_code=status.HTTP_201_CREATED)
async def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    db_album = models.Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

@router.get("/", response_model=List[Album], status_code=status.HTTP_200_OK)
async def get_albums(db: Session = Depends(get_db)):
    return db.query(models.Album).all()

@router.get("/{album_id}", response_model=Album, status_code=status.HTTP_200_OK)
async def get_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(models.Album).filter(models.Album.album_id == album_id).first()
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@router.delete("/{album_id}", status_code=status.HTTP_200_OK)
async def delete_album(album_id: int, db: Session = Depends(get_db)):
    album = db.query(models.Album).filter(models.Album.album_id == album_id).first()
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    db.delete(album)
    db.commit()
    return {"detail": "Album deleted successfully"}

@router.put("/{album_id}", response_model=Album, status_code=status.HTTP_200_OK)
async def update_album(album_id: int, album: AlbumCreate, db: Session = Depends(get_db)):
    db_album = db.query(models.Album).filter(models.Album.album_id == album_id).first()
    if db_album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    for key, value in album.dict().items():
        setattr(db_album, key, value)
    db.commit()
    db.refresh(db_album)
    return db_album
