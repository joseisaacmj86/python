
# uvicorn app.main:app --reload

from fastapi import FastAPI
from app.database import engine
import app.models as models
from routers import search, OAuth2_jwt_users, users, extract_metadata_mp3
import uvicorn

# Crea todas las tablas en la base de datos si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluye los routers
app.include_router(search.router)
app.include_router(OAuth2_jwt_users.router)
app.include_router(users.router)
app.include_router(extract_metadata_mp3.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)