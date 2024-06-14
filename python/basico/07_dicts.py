### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre": "jose",
                 "Apellido": "alvarez", "Edad": 37, 1: "Python"}

my_dict = {
    "nombre": "jose",
    "Apellido": "alvarez",
    "Edad": 37,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))


# Busqueda

print(my_dict[1])
print(my_dict["nombre"])

print("alvarez" in my_dict)
print("Apellido" in my_dict)


# Inserción

my_dict["calle"] = "calle 18"
print(my_dict)


# Actualización

my_dict["nombre"] = "juanito"
print(my_dict["nombre"])


# Eliminación

del my_dict["calle"]
print(my_dict)


# Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["nombre", 1, "piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("nombre", 1, "piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "18")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
