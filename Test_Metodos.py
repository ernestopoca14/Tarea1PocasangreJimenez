# Ernesto Pocasangre
# Luis Jimenez
# Tarea 1
# Pruebas
# ERR4 -10
import random  # Se importa la libreria random
import math  # Se importa la libreria math
from Metodos import multiple_op  # Se importa función de Metodos
from Metodos import verify_array_op  # Se importa función de Metodos

print("Tipos de errores: ")  # Imprime una lista de posibles errores
print("ERROR #1 Valor ingresado no fue un numero valido")  # Imprime texto
print("ERROR #2 Valor ingresado no fue un arreglo")  # Imprime texto
print("ERROR #3 Valores en el arreglo no fueron numeros validos\n")
# Imprime texto
x = random.randint(1, 10)  # Le otorga un valor aleatorio a "x" entre 1 y 10
print("Prueba 1 con multiple_op")  # Imprime texto
print("Entrada: ", x)  # Imprime la entrada aleatoria
y = multiple_op(x)  # Le otorga a "y" el valor de la función multiple_op(x)
assert y[0] == x * x  # Verifica que el primer valor de "y" sea en efecto x*x
assert y[1] == 2 ** x  # Verifica que el segundo valor de "y" sea 2^x
assert y[2] == math.factorial(x)  # Verifica que el tercer valor de "y" sea X!
print("El arreglo obtenido es: ", y, "\n")
# Imprime el resultado del arreglo y da un espacio entre lineas

k = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
# Establece a "k" como un array de tres numéros aleatorios entre 1 y 10
print("Prueba 2 con verify_array_op")  # Imprime el texto Prueba 2
print("Entrada: ", k)  # Imprime la entrada aleatoria
m = verify_array_op(k)
# Define a "m" como la salida de verify_array_op en función de "k"
i = 0  # Empieza un contador
for array in m:  # Comienza un loop por cada elemento de "m"
    assert array[0] == k[i] * k[i]
    # Asegura que el primer valor del array sea la multiplicación de k[i]*k[i]
    assert array[1] == 2 ** k[i]
    # Asegura que el segundo valor del array sea 2^k[i]
    assert array[2] == math.factorial(k[i])
    # Asegura que el tercer valor del array sea k[i]!
    i = i + 1
    # Se aumenta el contador para analizar el siguiente arreglo
print("El arreglo de arreglos obtenido es: ", m, "\n\n")
# Imprime el arreglo de arreglos y da dos espacios de lineas


x = "Prueba"  # Define a "x" como un string
print("Prueba 3 con multiple_op")  # Imprime el texto Prueba 3
print("Entrada: ", x)  # Imprime la entrada, en este caso un string
y = multiple_op(x)  # Define a "y" como la salida de multiple_op(x)
assert y == 1
# Se asegura que si "y" no es un numero valido, se genere el error
print("El arreglo obtenido es: Error #", y, "\n")
# Imprime el resultado y da un espacio de linea


k = [random.randint(1, 10), random.randint(1, 10), "Prueba"]
# Asigna a "k" un arreglo con2 numeros aleatorios y un elemento string
print("Prueba 4 con verify_array_op")  # Imprime el texto Prueba 4
print("Entrada: ", k)  # Imprime la entrada de un arreglo con string
m = verify_array_op(k)  # Define a m como la salida de verify_array_op(k)
assert (m == 3) or (m == 2)
# Asegura que si todos los elementos de k no son numereros validos o si k no
# es un arreglo, m genere un error
print("El arreglo de arreglos obtenido es: Error #", m)  # Imprime las salida
