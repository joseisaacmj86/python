
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

@router.get("/", status_code=status.HTTP_200_OK)
async def get_artist_data(search_data: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if not search_data:
        raise HTTPException(status_code=400, detail="search_data parameter is required")
    
    keywords = search_data.split()
    artist_filters = []
    album_filters = []
    song_filters = []

    for keyword in keywords:
        
        artist_keyword_filter = func.lower(models.Artist.artist).ilike(f"%{keyword.lower()}%")
        artist_filters.append(artist_keyword_filter)
        
        album_keyword_filter = func.lower(models.Album.album).ilike(f"%{keyword.lower()}%")
        album_filters.append(album_keyword_filter)

        song_keyword_filter = func.lower(models.Song.title).ilike(f"%{keyword.lower()}%")
        song_filters.append(song_keyword_filter)
    
    artist_query = db.query(models.Artist).filter(and_(*artist_filters))
    album_query = db.query(models.Album).filter(and_(*album_filters))
    song_query = db.query(models.Song).filter(and_(*song_filters))

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
            "artist": artist.artist,
            "genre": artist.genre,            
            "albums": []
        }

        artist_albums = db.query(models.Album).filter(models.Album.artist_id == artist.artist_id).all()
        for album in artist_albums:
            album_data = {
                "album_id": album.album_id,
                "artist_id": album.artist_id,
                "album": album.album,
                "year": album.year,
                "songs": []
            }

            artist_songs = db.query(models.Song).filter(models.Song.album_id == album.album_id).all()
            for song in artist_songs:
                song_data = {
                    "song_id": song.song_id,
                    "album_id": song.album_id,
                    "title": song.title,
                    "track_number": song.track_number,
                    "duration": song.duration,
                    "lyrics": song.lyrics
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
                "artist": artist.artist,
                "genre": artist.genre,            
                "albums": []
            }

            album_data = {
                "album_id": album.album_id,
                "artist_id": album.artist_id,
                "album": album.album,
                "year": album.year,
                "songs": []
            }

            artist_songs = db.query(models.Song).filter(models.Song.album_id == album.album_id).all()
            for song in artist_songs:
                song_data = {
                    "song_id": song.song_id,
                    "album_id": song.album_id,
                    "title": song.title,
                    "track_number": song.track_number,
                    "duration": song.duration,
                    "lyrics": song.lyrics
                }
                album_data["songs"].append(song_data)

            artist_data["albums"].append(album_data)
            result.append(artist_data)
           
    # Process songs
    for song in songs:
        artist_album = db.query(models.Album).filter(models.Album.album_id == song.album_id).first()
        if artist_album:
            artist = db.query(models.Artist).filter(models.Artist.artist_id == artist_album.artist_id).first()
            if artist:
                artist_data = {
                    "artist_id": artist.artist_id,
                    "artist": artist.artist,
                    "genre": artist.genre,            
                    "albums": []
                }

                album_data = {
                    "album_id": artist_album.album_id,
                    "artist_id": artist_album.artist_id,
                    "album": artist_album.album,
                    "year": artist_album.year,
                    "songs": []
                }

                song_data = {
                    "song_id": song.song_id,
                    "album_id": song.album_id,
                    "title": song.title,
                    "track_number": song.track_number,
                    "duration": song.duration,
                    "lyrics": song.lyrics
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
                "artist": artist["artist"],
                "genre": artist["genre"],
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
    


