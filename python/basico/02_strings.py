# formateo

name, surname, age = 'jose', 'isaac', 36

print(f'Mi nombre es {name} {surname} y tengo {age} años')

print('Mi nombre es {} {} y tengo {} años'.format(name, surname, age))

#otra forma
print('Mi nombre es {1} {0} y tengo {2} años'.format(name, surname, age))

print('Mi nombre es {n} {s} y tengo {a} años'.format(n=name, s=surname, a=age))

print(f'Mi nombre es {name} {surname} y tengo {age} años')


#formato usando %s y %d: esto sirve para que solo se imprima un dato de cierto tipo
print('Mi nombre es %s %s y tengo %d años' % (name, surname, age))

#formateo por inferencia
print(f'Mi nombre es {name} {surname} y tengo {age} años')

#desempaquecado de caracteres
languajes = "python"
a, b, c, d, e, f = languajes

print(a, b, c, d, e, f)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

languaje_splice = languajes[1:3]
print(languaje_splice)

languaje_splice = languajes[1:]
print(languaje_splice)

languaje_splice = languajes[0:5]
print(languaje_splice)

languaje_splice = languajes[-2]
print(languaje_splice)

languaje_splice = languajes[1:2:4]
print(languaje_splice)

#reverse
languaje_splice = languajes[::-1]
print(languaje_splice)




      


