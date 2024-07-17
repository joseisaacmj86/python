### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
#con % (porcentaje se calcula el modulo)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
        


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagram(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if(palabra1 == palabra2):
        return False
    else:
        palabra1 = palabra1.replace(" ", "")
        palabra2 = palabra2.replace(" ", "")
        palabra1 = sorted(palabra1)
        palabra2 = sorted(palabra2)
        if(palabra1 == palabra2):
            return True
        else:
            return False
    
    
    
my_anagram = is_anagram("Amor", "Roma")
if (my_anagram==True):
    print("Es un anagrama")
else:
    print("No es un anagrama")
    
    
    
    
def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))



"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def serie_fibonacci():
    a=0
    b=1
    #print(a)
    #print(b)
    for i in range(50):
        print(a)
        c=a+b
        a=b
        b=c
        print(c)
        
        
serie_fibonacci()


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

#comprueba si un numero es primo o no
#nota: con % obtenemos el modulo o residuo de una division
def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if(is_prime(6)==True):
    print("Es primo")
else:
    print("No es primo")
    
    
#otra forma de verificar si un numero es primo
import math

def is_prime2(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime2(10))  # False
print(is_prime2(7))   # True


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Ejemplos de uso
print(is_prime(10))  # False
print(is_prime(7))   # True
print(is_prime(29))  # True
print(is_prime(97))  # True

    
    

#genera los numeros primos desde 1 a 100
for i in range(1, 101):
    if(is_prime(i)==True):
        print(i)


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(cadena):
    cadena_len = len(cadena)
    reversed_cadena = ""
    for i in range(0, cadena_len):
        reversed_cadena += cadena[cadena_len - i - 1]
    return reversed_cadena


print(reverse("Hola mundo")) 