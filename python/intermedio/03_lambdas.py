
#lambda es una forma de definir funciones anónimas en Python

# Las funciones lambda pueden tener cualquier número de parámetros pero solo una expresión. 
# El resultado de la expresión es el valor devuelto por la función lambda. 
# Son útiles para definir funciones simples de una sola línea sin tener que usar la palabra clave def.

sum_values = lambda value1, value2: value1 + value2
print (sum_values(2,3))

sum_values = lambda value1, value2: print(value1 + value2)
sum_values(12,3)

sum_values = lambda value1, value2: print(value1*value2 -8)
sum_values(12,3)

sum_values = lambda x, y: x + y
print(sum_values(5, 3))

square = lambda x: x ** 2
print(square(4))

# Filtrar una lista para obtener solo los números pares:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

#Ordenar una lista de tuplas por el segundo elemento:
tuples = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)


#Convertir una lista de grados Celsius a Fahrenheit:
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(fahrenheit)

# Elevar cada número en una lista a la tercera potencia:
numbers = [1, 2, 3, 4, 5]
cubed = list(map(lambda x: x ** 3, numbers))
print(cubed)


#Comprobar si una cadena es un palíndromo:
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome('radar'))  
print(is_palindrome('python'))

#Encontrar el mayor de dos números:
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))


#Comprobar si un número es positivo, negativo o cero:
check_number = lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Zero')
print(check_number(10))
print(check_number(-5)) 
print(check_number(0)) 




#Usar lambdas en una función de orden superior:
def apply_function(x, func):
    return func(x)

result = apply_function(5, lambda x: x ** 2)
print(result) 




#usando def
def sum_two_values(
    value1, value2): return value1 + value2

print(sum_two_values(2, 4))



def multiply_values(value1, value2): return value1 * value2 - 3

print(multiply_values(2, 4))



def sum_three_values(value):
    return lambda value1, value2: value1 + value2 + value

print(sum_three_values(5)(2, 4))
