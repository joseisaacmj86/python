#Manejo de ficheros

import os

import json

import csv

import xml

"""
# Leer, escribir y sobrescribir si ya existe
# la "r" permiso de lectura, la "w" permiso de escritura,  la "w+" permiso de lectura y escritura
txt_file = open("python/intermedio/my_document.txt", 'r+')
# print(txt_file.read()) #lee todo el fichero
print(txt_file.read(15)) #leer una parte del fichero

print(txt_file.readline()) # leer por linea
print(txt_file.readline()) #  si se pone de seguido lee la siguiente linea
print(txt_file.readlines()) # readlines (plural) lee todo e imdoca los saltos de linea con (\n) 
for line in txt_file.readlines():
    print(line)


# Asegúrate de que el archivo exista
file_path = "python/intermedio/my_document.txt"

# Verifica si el archivo existe
if os.path.exists(file_path):
    # Abre el archivo con permisos de lectura y escritura
    with open(file_path, "r+") as txt_file:
        print(txt_file.read())
else:
    print(f"El archivo {file_path} no existe.")



# Obtener la ruta absoluta del archivo
file_path = os.path.abspath("python/intermedio/my_document.txt")

# Verifica si el archivo existe
if os.path.exists(file_path):
    # Abre el archivo con permisos de lectura y escritura
    with open(file_path, "r+") as txt_file:
        print(txt_file.read())
else:
    print(f"El archivo {file_path} no existe.")



txt_file.write(    "Mi nombre es Jose\nMi apellido es Alvarez\n37 años\nY mi lenguaje preferido es Python")
txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

"""



# .json file

json_file = open("python/intermedio/my_document.json", "w+")

json_test = {
    "name": "jose",
    "surname": "alvarez",
    "age": 37,
    "languages": ["Python", "PHP", "JS"],
    "website": "https://nnnn.dev"}


# json_file.write(json_test) # esto da error

# json.dump(json_test, json_file) # asi se escribe en una linea

json.dump(json_test, json_file, indent=2) # asi le aplicamos indentación

json_file.close()



with open("python/intermedio/my_document.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("python/intermedio/my_document.json"))

print(json_dict)
print(type(json_dict))
print(json_dict["name"])




# .csv file

csv_file = open("python/intermedio/my_document.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["jose", "alvarez", 37, "Python", "https://nnnn.dev"])
csv_writer.writerow(["diego", "", 18, "SQL", ""])

csv_file.close()

with open("python/intermedio/my_document.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?


