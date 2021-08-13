# Ernesto Pocasangre
# Luis Jimenez
# Tarea 1 MT - 7003
# Punto 3
import math  # Se importa la librería math


def multiple_op(X):  # función con un único parámetro de entrada
    '''
    Entrada: numero entero positivo (X)
    Salida: Arreglo de numeros enteros positivos (Y)
    El metodo hace la verificación del tipo de entrada
    La salida es de la forma [X * X, 2 ** X, X!]
    '''
    if (type(X) is int) and (X > 0):
        # Verifica si es un entero positivo
        Y = [X * X, 2 ** X, math.factorial(X)]
        # Hace un arreglo con las caracteristicas solicitadas
        return Y  # Retorna el arreglo creado
    return 1  # Retorna el ERROR #1 Valor ingresado no fue un numero valido


def verify_array_op(X):  # función con un único parámetro de entrada
    '''
    Entrada: arreglo de numeros enteros positivos (X)
    Salida: Arreglo de arreglo de numeros enteros positivos (Y)
    El metodo hace la verificación del tipo de entrada
    La salida es un arreglo que tiene como elementos arreglos creados
    con el metodo de multiple_op
    '''
    Y = []  # Crea un arreglo vacio
    if type(X) is not list:  # Verifica si el valor ingresado no es una lista
        return 2  # Arroja ERROR #2 Valor ingresado no fue un arreglo
    for num in X:  # Hace un loop por cada elemento en el arreglo
        if (type(num) is not int) or (num < 0):
            # Condición que verifica si el elemento no es un numero valido
            return 3  # Retorna el ERROR #3 Valores en el
# arreglo no fueron numeros validos
        Y.append(multiple_op(num))
        # Añade la salida de multiple_op del elemento inicial al arreglo nuevo
    return Y  # Retorna el arreglo de arreglos
