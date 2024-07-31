from fastapi import FastAPI
from routers import products, api_user, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles


app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users_db.router)

app.include_router(api_user.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.mount("/static", StaticFiles(directory="static"), name="static") # nos sirve para exponer recursos estaticos como imagenes


# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

# importatnte: que las peticiones sean asincronas. Ej: async def main():

#nota: para generar documentacion usar: Redocly http://127.0.0.1:8000/redoc o Swagger http://127.0.0.1:8000/docs

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}/{q}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/page")
async def page():
    return {"my_page": "https://tawk.to/666a10e19a809f19fb3cfb7b"}