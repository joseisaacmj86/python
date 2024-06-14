### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"



# Excepcion base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error")



# Flujo completo de una excepcion: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecucion continúa")




# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")




# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
