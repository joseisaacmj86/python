from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://python:python@localhost:3306/music_player"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

# bind: es el parametro por donde pasamos la conexion para estrablecer la session de la db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# nos permite hacer toda la interaccion con la db
Base = declarative_base()
