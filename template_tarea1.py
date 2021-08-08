# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np
from statistics import mode, mean, median

input_dir='Utilidades/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename=input_dir+'energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) que van desde T1 hasta RH_9 y funciona para números solamente.
# En su forma actual, esta línea NO LEE datos de tiempo. Para cambios en el mismo, usar la referencia de la funcion genfromtxt como guia
datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = range(3,21))

# Su código va aquí...

def extraerDatos():

    T4 = [] #Lista en la que se almacenaran los valores de la temperatura en la oficina
    
    cant = len(datos) #Cantidad de filas de la matriz, utilizado como punto de parada
    cont = 0 #Inicios

    #Extrae los datos de T4 "Temperatura en la oficina"
    while(cont < cant):
        
        T4.append(datos[cont][6]) #Se añaden los datos extraidos del archivo para la columna correspondiente "T4"
        cont += 1 #Incrementa contador para extraer el dato T4 de la siguiente fila
        
    T4.sort() #Se hizo uso de la funcion de python para listas "sort", con el fin de poder realizar el calculo de la mediana de forma eficiente

    promedio = mean(T4)
    mediana = median(T4)
    moda = mode(T4)
    print(promedio)
    print(mediana)
    print(moda)

extraerDatos()
    

