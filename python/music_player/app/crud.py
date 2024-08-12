from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database


def add_data(data, db: Session):
    messages = []  # Usa una lista para almacenar los mensajes

    for song_filename, song_data in data.items():
        # Extrae los datos de la canción del diccionario
        artist_name = song_data['artist']
        album_name = song_data['album']
        title = song_data['title']
        year = song_data['year']
        genre = song_data['genre']
        track_number = song_data['track_number']
        duration = song_data['duration']
        lyrics = song_data['lyrics']
        
        # Consulta o crea el artista
        artist = db.query(models.Artist).filter(models.Artist.artist == artist_name).first()
        if artist is None:
            new_artist = models.Artist(
                artist=artist_name,
                genre=genre
            )
            db.add(new_artist)
            db.commit()
            db.refresh(new_artist)
            artist_id = new_artist.artist_id
        else:
            artist_id = artist.artist_id

        # Consulta o crea el álbum
        album = db.query(models.Album).filter(models.Album.album == album_name).first()
        if album is None:
            new_album = models.Album(
                artist_id=artist_id,
                album=album_name,
                year=year if isinstance(year, int) else None  # Convertir año a int si es necesario
            )
            db.add(new_album)
            db.commit()
            db.refresh(new_album)
            album_id = new_album.album_id
        else:
            album_id = album.album_id

        # Consulta o crea la canción
        song_data_db = db.query(models.Song).filter(models.Song.title == title).first()
        if song_data_db is None:
            new_song = models.Song(
                album_id=album_id,
                title=title,
                track_number=track_number,
                duration=duration,
                lyrics=lyrics
            )
            db.add(new_song)
            db.commit()
            db.refresh(new_song)
            messages.append({"message": f"Song '{title}' added successfully"})
        else:
            messages.append({"message": f"Song '{title}' already exists"})
    
    return {"messages": messages}