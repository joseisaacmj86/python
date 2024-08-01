from pydantic import BaseModel


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



"""
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
        
"""