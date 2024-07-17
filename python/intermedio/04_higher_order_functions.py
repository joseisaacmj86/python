
"""
    Las funciones de orden superior (o funciones de alto orden) son funciones que 
    cumplen al menos una de las siguientes condiciones:

    1. Toman una o más funciones como argumentos.
    2. Devuelven una función como resultado.

    Estas funciones son muy útiles en la programación funcional y permiten un alto 
    nivel de abstracción y reutilización de código. Veamos algunos ejemplos para 
    ilustrar esto.
"""

#Funciones que toman otras funciones como argumentos
#map: Aplica una función a cada elemento de una lista.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Salida: [1, 4, 9, 16, 25]


#filter: Filtra los elementos de una lista según una función que devuelve True o False.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Salida: [2, 4, 6, 8, 10]


#reduce: Aplica una función acumulativa a los elementos de una lista, reduciéndola 
# a un solo valor.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Salida: 15




#Funciones que devuelven otras funciones
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
print(double(5))  # Salida: 10

triple = make_multiplier(3)
print(triple(5))  # Salida: 15




# Uso combinado de ambas propiedades
# una función que toma otra función como argumento y devuelve una nueva función.
def apply_twice(func):
    return lambda x: func(func(x))

def increment(x):
    return x + 1

increment_twice = apply_twice(increment)
print(increment_twice(5))  # Salida: 7




"""
Aplicaciones de funciones de orden superior
Las funciones de orden superior son comunes en muchas bibliotecas y marcos de trabajo.
Aquí hay algunas aplicaciones típicas:

1. Transformación de datos: Utilizar map, filter y reduce para transformar y reducir 
colecciones de datos.
2. Decoradores: En Python, los decoradores son funciones de orden superior que 
modifican el comportamiento de otras funciones.
3. Callbacks: Funciones de orden superior se utilizan para manejar eventos y asincronía, 
como en addEventListener en JavaScript o callbacks en Python.
"""

def my_decorator(func):
    def wrapper():
        print("Algo está sucediendo antes de que se llame a la función.")
        func()
        print("Algo está sucediendo después de que se llama a la función.")
    return wrapper

@my_decorator
def say_hello():
    print("Hola!")

say_hello()
# Salida:
# Algo está sucediendo antes de que se llame a la función.
# Hola!
# Algo está sucediendo después de que se llama a la función.






from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))




#Closures

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))



#Built-in Higher Order Functions

numbers = [2, 5, 10, 21, 3, 30]



# Map

def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))




# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))



# Reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))

