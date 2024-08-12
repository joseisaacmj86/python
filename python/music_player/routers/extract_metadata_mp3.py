
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import Dict
from app.database import SessionLocal
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TYER, TCON, TRCK, TCOM, COMM, USLT, APIC, TPUB, TIT1, TOAL, TDRL, WCOP
from app.crud import add_data

router = APIRouter(prefix="/extract",
                   tags=["extract"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def extract_year_from_mp3(file_path):
    try:
        audio = ID3(file_path)
        tdrc_tag = audio.get('TDRC')
        if tdrc_tag:
            return tdrc_tag.text[0].year
        else:
            return "Año no encontrado"
    except Exception as e:
        return f"Error al leer el archivo: {e}"

def get_mp3_metadata(file_path):
    audio = MP3(file_path, ID3=ID3)
    metadata = {
        "title": audio.get("TIT2", "Unknown Title").text[0] if audio.get("TIT2") else "Unknown Title",
        "artist": audio.get("TPE1", "Unknown Artist").text[0] if audio.get("TPE1") else "Unknown Artist",
        "album": audio.get("TALB", "Unknown Album").text[0] if audio.get("TALB") else "Unknown Album",
        # Usa la función extract_year_from_mp3 para obtener el año
        "year": extract_year_from_mp3(file_path),
        "genre": audio.get("TCON", "Unknown Genre").text[0] if audio.get("TCON") else "Unknown Genre",
        "track_number": audio.get("TRCK", "Unknown Track Number").text[0] if audio.get("TRCK") else "Unknown Track Number",
        "composer": audio.get("TCOM", "Unknown Composer").text[0] if audio.get("TCOM") else "Unknown Composer",
        "duration": audio.info.length,
        "comments": audio.get("COMM::'eng'", "No Comments").text[0] if audio.get("COMM::'eng'") else "No Comments",
        "lyrics": audio.get("USLT::'eng'", "No Lyrics").text[0] if audio.get("USLT::'eng'") else "No Lyrics",
        "album_art": "No Album Art" if "APIC:" not in audio else "Has Album Art",
        "publisher": audio.get("TPUB", "Unknown Publisher").text[0] if audio.get("TPUB") else "Unknown Publisher",
        "grouping": audio.get("TIT1", "Unknown Grouping").text[0] if audio.get("TIT1") else "Unknown Grouping",
        "original_album": audio.get("TOAL", "Unknown Original Album").text[0] if audio.get("TOAL") else "Unknown Original Album",
        "release_date": audio.get("TDRL", "Unknown Release Date").text[0] if audio.get("TDRL") else "Unknown Release Date",
        "copyright": audio.get("WCOP", "Unknown Copyright").text[0] if audio.get("WCOP") else "Unknown Copyright"
    }
    return metadata

def extract_metadata_from_library(directory_path):
    mp3_files = [f for f in os.listdir(directory_path) if f.endswith('.mp3')]
    all_metadata = {}
    
    for mp3_file in mp3_files:
        file_path = os.path.join(directory_path, mp3_file)
        metadata = get_mp3_metadata(file_path)
        all_metadata[mp3_file] = metadata

    return all_metadata
    

@router.get("/")
def get_metadata_from_library(directory_path: str, db: Session = Depends(get_db)):
    if not os.path.isdir(directory_path):
        raise HTTPException(status_code=404, detail="Directory not found")
    
    metadata = extract_metadata_from_library(directory_path)
    return add_data(metadata, db)

