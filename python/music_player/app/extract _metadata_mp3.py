from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TYER, TCON, TRCK, TCOM, TLEN, COMM, USLT, APIC, TPUB, TIT1, TOAL, TDRL, WCOP

def get_mp3_metadata(file_path):
    audio = MP3(file_path, ID3=ID3)
    metadata = {
        "title": audio.get("TIT2", "Unknown Title"),
        "artist": audio.get("TPE1", "Unknown Artist"),
        "album": audio.get("TALB", "Unknown Album"),
        "year": audio.get("TYER", "Unknown Year"),
        "genre": audio.get("TCON", "Unknown Genre"),
        "track_number": audio.get("TRCK", "Unknown Track Number"),
        "composer": audio.get("TCOM", "Unknown Composer"),
        "duration": audio.info.length,
        "comments": audio.get("COMM::'eng'", "No Comments"),
        "lyrics": audio.get("USLT::'eng'", "No Lyrics"),
        "album_art": "No Album Art" if "APIC:" not in audio else "Has Album Art",
        "publisher": audio.get("TPUB", "Unknown Publisher"),
        "grouping": audio.get("TIT1", "Unknown Grouping"),
        "original_album": audio.get("TOAL", "Unknown Original Album"),
        "release_date": audio.get("TDRL", "Unknown Release Date"),
        "copyright": audio.get("WCOP", "Unknown Copyright")
    }
    return metadata

# Ejemplo de uso:
file_path = "library/Trivium - Until The World Goes Cold (Music Video).mp3"
metadata = get_mp3_metadata(file_path)
print(metadata)
