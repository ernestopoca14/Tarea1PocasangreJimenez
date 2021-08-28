# Ernesto Pocasangre
# Luis Jimenez
# Tarea 2 MT - 7003
from _thread import *  # Importación de librerias
from threading import *
import time
import argparse

# Implementación del modulo argparse para introducir argumentos desde el cmd
# que se utilizaran mas adelante
parser = argparse.ArgumentParser(description='Calcular tiempos')
parser.add_argument('num', type=int, help='Numero de elementos del arreglo')
parser.add_argument('imp', type=int, help='Tipo de impresion')
args = parser.parse_args()


# Definición de la función que crea un arreglo a partir de un
# parametro introducido
def crearArreglo(num):
    arreglo = []
    for elemento in range(num):
        arreglo.append(int(elemento))
    return arreglo


# Definición de una función que hace la potenciación para cada
# elemento del arreglo creado
def potencia(arreglo):
    arreglo2 = []
    for elemento in arreglo:
        arreglo2.append(int(elemento**2))
        time.sleep(0.1)
    return arreglo2


# Se crea el arreglo a partir del parametro ingresado en el cmd
x = crearArreglo(args.num)
# Se cuenta el tiempo inicial
start1 = time.time()
# Se llama a la funcion potencia con el arreglo creado en 1 hilo
t = Thread(target=potencia, args=(x,))
# Se inicia el procedimiento
t.start()
# Se llama al metodo de join
t.join()
# Se cuenta el tiempo final
stop1 = time.time()
# Se hace la resta vara ver cuanto duró el proceso
tiempo1 = stop1 - start1

# Se divide el arreglo en 4 partes para ser procesado en 4 hilos
y = args.num // 4
x1 = x[:y]
x2 = x[y:2 * y]
x3 = x[2 * y:3 * y]
x4 = x[3 * y:]

# Se cuenta el tiempo inicial
start2 = time.time()

# Se llama a la funcion de potencia para cada hilo con una porcion del arreglo
t1 = Thread(target=potencia, args=(x1,))
t2 = Thread(target=potencia, args=(x2,))
t3 = Thread(target=potencia, args=(x3,))
t4 = Thread(target=potencia, args=(x4,))

# Se inicia el procedimiento
t1.start()
t2.start()
t3.start()
t4.start()

# Se llama al procedimiento de join
t1.join()
t2.join()
t3.join()
t4.join()

# Se cuenta el tiempo final
stop2 = time.time()
# Se hace la resta vara ver cuanto duró el proceso
tiempo2 = stop2 - start2

# Se hace la comparacion para verificar si se imprimen los datos
# o si se hace un archivo .txt con los tiempos
if args.imp:
    with open('resultados.txt', 'w') as file_object:
        file_object.write('Tiempo de la operacion para 1 hilo: ')
        file_object.write(str(tiempo1)+'\n')
        file_object.write('Tiempo de la operacion para 4 hilos: ')
        file_object.write(str(tiempo2))
else:
    print('Tiempo de la operacion para 1 hilo: ')
    print(str(tiempo1)+'\n')
    print('Tiempo de la operacion para 4 hilos: ')
    print(str(tiempo2))
