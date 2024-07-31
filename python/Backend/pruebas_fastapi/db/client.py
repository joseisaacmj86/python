
# MongoDB client 

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

from pymongo import MongoClient

# Descomentar el db_client local o remoto correspondiente

# Base de datos local MongoDB
# db_client = MongoClient().local


# Base de datos remota MongoDB Atlas (https://mongodb.com)
uri ="mongodb+srv://joseisaac:joseisaac@projectswithpython.h2uetva.mongodb.net/?retryWrites=true&w=majority&appName=projectsWithPython"
db_client = MongoClient(uri).test
# Send a ping to confirm a successful connection
#try:
#    db_client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#    print(e)

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/
