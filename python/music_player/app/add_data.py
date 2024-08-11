
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter(prefix="/add_data",
                   tags=["add_data"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_data(data: schemas.ArtistCreate, db: Session = Depends(get_db)):
    # Verificar si el artista ya existe
    artist = db.query(models.Artist).filter(models.Artist.artist_id == data.artist_id).first()
    if artist:
        raise HTTPException(status_code=400, detail="Artist already exists")

    # Crear el artista
    new_artist = models.Artist(
        artist_id=data.artist_id,
        first_name=data.first_name,
        last_name=data.last_name,
        band_name=data.band_name
    )
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)

    # Crear los álbumes y canciones
    for album in data.albums:
        new_album = models.Album(
            album_id=album.album_id,
            artist_id=album.artist_id,
            name_album=album.name_album,
            year=album.year
        )
        db.add(new_album)
        db.commit()
        db.refresh(new_album)

        for song in album.songs:
            new_song = models.Song(
                song_id=song.song_id,
                album_id=song.album_id,
                song_name=song.song_name,
                duration_time=song.duration_time
            )
            db.add(new_song)

    db.commit()
    return {"message": "Data added successfully"}