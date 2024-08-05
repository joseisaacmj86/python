
# uvicorn app.main:app --reload

from fastapi import FastAPI
from app.database import engine
import app.models as models
from routers import registros, artists, albums, songs, search
import uvicorn

# Crea todas las tablas en la base de datos si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluye los routers
app.include_router(registros.router, prefix="/registers", tags=["registers"])
app.include_router(artists.router)
app.include_router(albums.router)
app.include_router(songs.router)
app.include_router(search.router)  # Asegúrate de incluir el router de búsqueda

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)