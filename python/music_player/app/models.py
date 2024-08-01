
from sqlalchemy import Column, Integer, String, ForeignKey, Time
from app.database import Base
from sqlalchemy.orm import relationship


class Ingreso(Base):
    __tablename__ = "registrodeingreso"

    id = Column(Integer, primary_key=True, index=True)
    documentoingreso = Column(String(11))
    nombrepersona = Column(String(100))
    
   

class Artist(Base):
    __tablename__ = "artists"

    artist_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    band_name = Column(String(255))

class Album(Base):
    __tablename__ = "albums"

    album_id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey("artists.artist_id"), nullable=False)
    name_album = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)

class Cancion(Base):
    __tablename__ = "songs"

    song_id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("albums.album_id"), nullable=False)
    song_name = Column(String(50), nullable=False)
    duration_time = Column(String(50), nullable=False)

"""
class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    band_name = Column(String, index=True)
    albums = relationship('Album', back_populates='artist')

class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    name_album = Column(String, index=True)
    year = Column(Integer)
    songs = relationship('Song', back_populates='album')
    artist = relationship('Artist', back_populates='albums')

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey('albums.id'))
    song_name = Column(String, index=True)
    duration_time = Column(String)
    album = relationship('Album', back_populates='songs')



class User(Base):
    # nombre de la tabla
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
"""

   