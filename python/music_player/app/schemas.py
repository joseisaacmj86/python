from pydantic import BaseModel
from typing import List



class ArtistBase(BaseModel):
    first_name: str
    last_name: str
    band_name: str | None = None

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    artist_id: int

    class Config:
        orm_mode = True

class AlbumBase(BaseModel):
    artist_id: int
    name_album: str
    year: int

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    album_id: int

    class Config:
        orm_mode = True

class CancionBase(BaseModel):
    album_id: int
    song_name: str
    duration_time: str

class CancionCreate(CancionBase):
    pass

class Cancion(CancionBase):
    song_id: int

    class Config:
        orm_mode = True



class IngresoBase(BaseModel):
    documentoingreso: str
    nombrepersona: str
    
class IngresoBase2(BaseModel):
    id: int
    documentoingreso: str
    nombrepersona: str


class Cancion(BaseModel):
    song_id: int
    album_id: int
    song_name: str
    duration_time: str
    
    class Config:
        orm_mode = True




# Schemas para add_data
class SongCreate(BaseModel):
    song_id: int
    album_id: int
    song_name: str
    duration_time: str

class AlbumCreate(BaseModel):
    album_id: int
    artist_id: int
    name_album: str
    year: int
    songs: List[SongCreate]

class ArtistCreate(BaseModel):
    artist_id: int
    first_name: str
    last_name: str
    band_name: str
    albums: List[AlbumCreate]


#Schemas users
class User(BaseModel):
    username: str
    full_name: str
    email: str
    role: str
    type_license: str
    disabled: bool


class UserPass(User):
    password: str