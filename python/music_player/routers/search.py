# busqueda por artista, albums y canciones, no sensible a mayusculas y trae varios resultado cuando hay mas de una 
# coincidencia en la db
from fastapi import APIRouter, HTTPException, Depends, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func
from typing import List, Optional
from app.database import SessionLocal
import app.models as models

router = APIRouter(prefix="/search",
                   tags=["search"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search", status_code=status.HTTP_200_OK)
async def get_artist_data(search_data: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if not search_data:
        raise HTTPException(status_code=400, detail="search_data parameter is required")
    
    keywords = search_data.split()
    artist_filters = []
    album_filters = []
    song_filters = []

    for keyword in keywords:
        keyword_filter = or_(
            func.lower(models.Artist.first_name).ilike(f"%{keyword.lower()}%"),
            func.lower(models.Artist.last_name).ilike(f"%{keyword.lower()}%"),
            func.lower(models.Artist.band_name).ilike(f"%{keyword.lower()}%")
        )
        artist_filters.append(keyword_filter)
        
        album_keyword_filter = func.lower(models.Album.name_album).ilike(f"%{keyword.lower()}%")
        album_filters.append(album_keyword_filter)

        song_keyword_filter = func.lower(models.Cancion.song_name).ilike(f"%{keyword.lower()}%")
        song_filters.append(song_keyword_filter)
    
    artist_query = db.query(models.Artist).filter(and_(*artist_filters))
    album_query = db.query(models.Album).filter(and_(*album_filters))
    song_query = db.query(models.Cancion).filter(and_(*song_filters))

    artists = artist_query.all()
    albums = album_query.all()
    songs = song_query.all()
    # return {"artistas": artists}, {"albums":albums}, {"canciones":songs}
    if not artists and not albums and not songs:
        raise HTTPException(status_code=404, detail="Artist, Album, or Song not found")

    result = []

    # Process artists
    for artist in artists:
        artist_data = {
            "artist_id": artist.artist_id,
            "first_name": artist.first_name,
            "last_name": artist.last_name,
            "band_name": artist.band_name,
            "albums": []
        }

        artist_albums = db.query(models.Album).filter(models.Album.artist_id == artist.artist_id).all()
        for album in artist_albums:
            album_data = {
                "album_id": album.album_id,
                "artist_id": album.artist_id,
                "name_album": album.name_album,
                "year": album.year,
                "songs": []
            }

            artist_songs = db.query(models.Cancion).filter(models.Cancion.album_id == album.album_id).all()
            for song in artist_songs:
                song_data = {
                    "song_id": song.song_id,
                    "album_id": song.album_id,
                    "song_name": song.song_name,
                    "duration_time": song.duration_time
                }
                album_data["songs"].append(song_data)

            artist_data["albums"].append(album_data)

        result.append(artist_data)

    # Process albums
    for album in albums:
        artist = db.query(models.Artist).filter(models.Artist.artist_id == album.artist_id).first()
        if artist:
            artist_data = {
                "artist_id": artist.artist_id,
                "first_name": artist.first_name,
                "last_name": artist.last_name,
                "band_name": artist.band_name,
                "albums": []
            }

            album_data = {
                "album_id": album.album_id,
                "artist_id": album.artist_id,
                "name_album": album.name_album,
                "year": album.year,
                "songs": []
            }

            artist_songs = db.query(models.Cancion).filter(models.Cancion.album_id == album.album_id).all()
            for song in artist_songs:
                song_data = {
                    "song_id": song.song_id,
                    "album_id": song.album_id,
                    "song_name": song.song_name,
                    "duration_time": song.duration_time
                }
                album_data["songs"].append(song_data)

            artist_data["albums"].append(album_data)
            result.append(artist_data)
            """
            # Check if artist_data already exists in result to avoid duplicates
            if artist_data not in result:
                result.append(artist_data)
            else:
                # If the artist already exists in result, append the new album to the existing artist's albums
                existing_artist_data = next(item for item in result if item["artist_id"] == artist.artist_id)
                existing_artist_data["albums"].append(album_data)
            """
    # Process songs
    for song in songs:
        artist_album = db.query(models.Album).filter(models.Album.album_id == song.album_id).first()
        if artist_album:
            artist = db.query(models.Artist).filter(models.Artist.artist_id == artist_album.artist_id).first()
            if artist:
                artist_data = {
                    "artist_id": artist.artist_id,
                    "first_name": artist.first_name,
                    "last_name": artist.last_name,
                    "band_name": artist.band_name,
                    "albums": []
                }

                album_data = {
                    "album_id": artist_album.album_id,
                    "artist_id": artist_album.artist_id,
                    "name_album": artist_album.name_album,
                    "year": artist_album.year,
                    "songs": []
                }

                song_data = {
                    "song_id": song.song_id,
                    "album_id": song.album_id,
                    "song_name": song.song_name,
                    "duration_time": song.duration_time
                }
                album_data["songs"].append(song_data)
                artist_data["albums"].append(album_data)
                result.append(artist_data)
                
    # return result
    
    unique_artists = {}

    for artist in result:
        artist_id = artist["artist_id"]
        if artist_id not in unique_artists:
            unique_artists[artist_id] = {
                "artist_id": artist["artist_id"],
                "first_name": artist["first_name"],
                "last_name": artist["last_name"],
                "band_name": artist["band_name"],
                "albums": []
            }
        
        for album in artist["albums"]:
            
            existing_album = next((a for a in unique_artists[artist_id]["albums"] if a["album_id"] == album["album_id"]), None)
            if existing_album:
               
                for song in album["songs"]:
                    if song not in existing_album["songs"]:
                        existing_album["songs"].append(song)
            else:
               
                unique_artists[artist_id]["albums"].append(album)

   
    result = list(unique_artists.values())
    return result
    


