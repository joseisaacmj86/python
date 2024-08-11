from mutagen.mp3 import MP3
from mutagen.id3 import ID3, ID3NoHeaderError

def print_available_tags(file_path):
    try:
        audio = MP3(file_path, ID3=ID3)
        tags = audio.tags
        for tag in tags:
            print(f"Tag: {tag}, Value: {tags[tag]}")
    except ID3NoHeaderError:
        print("No ID3 header found. The file might not have ID3 tags.")

# Ejemplo de uso:
file_path = "library/Trivium - Until The World Goes Cold [OFFICIAL VIDEO].mp3"
print_available_tags(file_path)
