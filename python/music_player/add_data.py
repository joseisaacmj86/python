import json
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

def add_data(data):
    db = SessionLocal()
    for artist in data:
        new_artist = models.Artist(
            artist_id=artist['artist_id'],
            first_name=artist['first_name'],
            last_name=artist['last_name'],
            band_name=artist['band_name']
        )
        db.add(new_artist)
        db.commit()
        
        for album in artist['albums']:
            new_album = models.Album(
                album_id=album['album_id'],
                artist_id=album['artist_id'],
                name_album=album['name_album'],
                year=album['year']
            )
            db.add(new_album)
            db.commit()
            
            for song in album['songs']:
                new_song = models.Song(
                    song_id=song['song_id'],
                    album_id=song['album_id'],
                    song_name=song['song_name'],
                    duration_time=song['duration_time']
                )
                db.add(new_song)
                db.commit()
    
    db.close()

if __name__ == "__main__":
    with open("data.json", "r") as file:
        data = json.load(file)
        add_data(data)
