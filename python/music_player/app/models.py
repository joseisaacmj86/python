
from sqlalchemy import Column, Integer, String, ForeignKey, Time, Boolean
from app.database import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)
    full_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    role = Column(String(255), index=True)
    type_license = Column(String(255), index=True)
    disabled = Column(Boolean, index=True)
    password = Column(String(255))
    
    

class Artist(Base):
    __tablename__ = "artists"

    artist_id = Column(Integer, primary_key=True, index=True)
    artist = Column(String(255), index=True)
    genre = Column(String(255), index=True)
    albums = relationship("Album", back_populates="artist")

class Album(Base):
    __tablename__ = "albums"

    album_id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey("artists.artist_id"))
    album = Column(String(255), index=True)
    year = Column(Integer)
    songs = relationship("Song", back_populates="album")
    artist = relationship("Artist", back_populates="albums")

class Song(Base):
    __tablename__ = "songs"

    song_id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("albums.album_id"))
    title = Column(String(255), index=True)
    track_number = Column(String(255))
    duration = Column(String(255))    
    lyrics = Column(String(255))
    album = relationship("Album", back_populates="songs")  