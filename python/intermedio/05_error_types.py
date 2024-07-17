
# SyntaxError se produce porq falta parentecis
# Descomentar para Error
# print "¡Hola comunidad!" 
print("¡Hola comunidad!")

from math import pi
import math


# NameError: de produce poque la variable no esta definida al ejecutar el print
# Descomentar para Error
# print(language)
language = "Spanish"  # Comentar para Error
print(language)



# IndexError: se produce cuando intentamos acceder a un indice que no existe
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error


# ModuleNotFoundError: se produce cuando se intenta importar un modulo que no existe
# import maths # Descomentar para Error


# AttributeError: se produce cuando se intenta acceder al atributo de un modulo y que
# dicho atributo no existe
# print(math.PI) # Descomentar para Error
print(math.pi)


# KeyError: se produce al intentar acceder al valor de un key q no existe o esta
#mal escrito
my_dict = {"Nombre": "jose", "Apellido": "alvarez", "Edad": 37, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])


# TypeError: se produce al intentar acceder al indice de una lista
# colocando el mismos entre "" o como cadena de texto o string
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])


# ImportError: se produce cuando se intenta acceder a la propieda de
# un modulo y que dicha propiedad no existe
# from math import PI # Descomentar para Error
print(pi)


# ValueError: se produce cuando se intenta tranformar
# un tipo de dato a otro, pero no respetando la naturaleza del dato
# que se intenta transformar
# my_int = int("10 Años") # Descomentar para Error
my_int = int("10")  
print(type(my_int))


# ZeroDivisionError
# print(4/0) # Descomentar para Error
print(4/2)
