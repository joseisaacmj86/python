# Regular Expressions

# Es un mecanismo que tenemos a lo largo de todos los lenguajes de programacion
# que nos sirve para inspeccionar si una cadena de texto tiene ciertos elementos.


import re

# match: intenta encontrar un patron

string1 = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
string2 = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", string1, re.I)
print(match)

match = re.match("Esta es la lección", string2, re.I)
print(match)

# Verificas si la coincidencia se encontró
if match:
    start, end = match.span()
    print(f"Match found from {start} to {end}")
else:
    print("No match found")


# start, end = match.span()
# print(string1[start:end])


match = re.match("Esta no es la lección", string2)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(string2[start:end])

print(re.match("Expresiones Regulares", string1))


# search

search = re.search("lección", string1, re.I)
print(search)
start, end = search.span()
print(string1[start:end])



# findall

findall = re.findall("lección", string1, re.I)
print(findall)




# split

print(re.split(":", string1))




# sub

print(re.sub("[l|L]ección", "LECCIÓN", string1))
print(re.sub("Expresiones Regulares", "RegEx", string1))





#Patterns

pattern = r"[lL]ección"
print(re.findall(pattern, string1))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, string1))

pattern = r"[0-9]"
print(re.findall(pattern, string1))
print(re.search(pattern, string1))

pattern = r"\d"
print(re.findall(pattern, string1))

pattern = r"\D"
print(re.findall(pattern, string1))

pattern = r"[l].*"
print(re.findall(pattern, string1))

email = "example@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "example@example.com.mx"
print(re.findall(pattern, email))
