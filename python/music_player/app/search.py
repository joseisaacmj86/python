from sqlalchemy.orm import Session
from app.database import SessionLocal
from sqlalchemy import or_
import app.models as models


# Busqueda por id, da como resultado un json con toda la data del artista icluidos albums y songs
def get_artist_data(artist_id: int, db: Session):
    artist = db.query(models.Artist).filter(models.Artist.artist_id == artist_id).first()
    if not artist:
        return None

    albums = db.query(models.Album).filter(models.Album.artist_id == artist_id).all()
    artist_data = {
        "artist_id": artist.artist_id,
        "first_name": artist.first_name,
        "last_name": artist.last_name,
        "band_name": artist.band_name,
        "albums": []
    }

    for album in albums:
        songs = db.query(models.Cancion).filter(models.Cancion.album_id == album.album_id).all()
        album_data = {
            "album_id": album.album_id,
            "artist_id": album.artist_id,
            "name_album": album.name_album,
            "year": album.year,
            "songs": []
        }

        for song in songs:
            song_data = {
                "song_id": song.song_id,
                "album_id": song.album_id,
                "song_name": song.song_name,
                "duration_time": song.duration_time
            }
            album_data["songs"].append(song_data)

        artist_data["albums"].append(album_data)

    return artist_data

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        