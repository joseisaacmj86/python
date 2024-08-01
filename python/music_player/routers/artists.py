from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
import app.models as models
from app.schemas import Artist, ArtistCreate

# router = APIRouter()
router = APIRouter(prefix="/artists",
                   tags=["artists"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Artist, status_code=status.HTTP_201_CREATED)
async def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    db_artist = models.Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

@router.get("/", response_model=List[Artist], status_code=status.HTTP_200_OK)
async def get_artists(db: Session = Depends(get_db)):
    return db.query(models.Artist).all()

@router.get("/{artist_id}", response_model=Artist, status_code=status.HTTP_200_OK)
async def get_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = db.query(models.Artist).filter(models.Artist.artist_id == artist_id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@router.delete("/{artist_id}", status_code=status.HTTP_200_OK)
async def delete_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = db.query(models.Artist).filter(models.Artist.artist_id == artist_id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(artist)
    db.commit()
    return {"detail": "Artist deleted successfully"}

@router.put("/{artist_id}", response_model=Artist, status_code=status.HTTP_200_OK)
async def update_artist(artist_id: int, artist: ArtistCreate, db: Session = Depends(get_db)):
    db_artist = db.query(models.Artist).filter(models.Artist.artist_id == artist_id).first()
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    for key, value in artist.dict().items():
        setattr(db_artist, key, value)
    db.commit()
    db.refresh(db_artist)
    return db_artist
