# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import math

input_dir='Utilidades/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename=input_dir+'energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) que van desde T1 hasta RH_9 y funciona para números solamente.
# En su forma actual, esta línea NO LEE datos de tiempo. Para cambios en el mismo, usar la referencia de la funcion genfromtxt como guia
datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = range(3,21))

def extraerDatos():

    T4 = [] #Lista en la que se almacenaran los valores de la temperatura en la oficina
    
    cant = len(datos) #Cantidad de filas de la matriz, utilizado como punto de parada
    cont = 0 #Inicios

    #Extrae los datos de T4 "Temperatura en la oficina"
    while(cont < cant):
        
        T4.append(datos[cont][6]) #Se añaden los datos extraidos del archivo para la columna correspondiente "T4"
        cont += 1 #Incrementa contador para extraer el dato T4 de la siguiente fila
        
    T4.sort() #Se hizo uso de la funcion de python para listas "sort", con el fin de poder realizar el calculo de la mediana de forma eficiente


    #MEDIDAS DE TENDENCIA
    promedio = st.mean(T4) #Se utiliza la librería "Statistics" para calcular el promedio
    mediana = st.median(T4) #Se utiliza la librería "Statistics" para calcular la mediana
    moda = st.mode(T4) #Se utiliza la librería "Statistics" para calcular la moda
    cuartiles = st.quantiles(T4) #Se utiliza la librería "Statistics" para calcular los cuartiles de T4
    
    Q1 = cuartiles[0] #De la lista de cuartiles se extrae el cuartil 1
    Q2 = cuartiles[1] #De la lista de cuartiles se extrae el cuartil 2
    Q3 = cuartiles[2] #De la lista de cuartiles se extrae el cuartil 3

    #Imprime medidas de tendencia
    print("\n\nMEDIDAS DE TENDENCIA")
    print("El promedio de las temperaturas T4 es: " + str(promedio))
    print("La mediana de las temperaturas T4 es: " + str(mediana))
    print("La moda de las temperaturas T4 es: " + str(moda))
    print("Los cuartiles son: " + " Q1 = " + str(Q1) + " Q2 = " + str(Q2) + " Q3 = " + str(Q3))



    #MEDIDAS DE DISPERCIÓN
    varianza = st.variance(T4) #Se utiliza la librería "Statistics" para calcular la varianza de T4
    desvEst = math.sqrt(varianza) #Se utiliza la librería "Math" para calcular la raiz cuadrada de la varianza (Desviacion Estandar)
    coefVar = (desvEst/promedio)*100 #Se realiza la formula de calculo del coeficiente de variacion
    rangoMuestral = T4[-1] - T4[0] #Se realiza la formula de calculo del rango muestral
    rangoInter = Q3 - Q1 #Se realiza la formula de calculo del rango intercuartilico
    

    #Imprime medidas de dispersión
    print("\n\nMEDIDAS DE DISPERSIÓN")
    print("La varianza de las temperaturas T4 es: " + " s^2 = " + str(varianza))
    print("La desviación estándar de las temperaturas T4 es: " + " s = " + str(desvEst))
    print("El coeficiente de variación de las temperaturas T4 es: " + " c.v = " + str(coefVar))
    print("El rango muestral de las temperaturas T4 es: " + " r = " + str(rangoMuestral))
    print("El rango intercuartílico de las temperaturas T4 es: " + " RIC = " + str(rangoInter))


    #Se itera sobre T4 para sacar la cantidad de repeticiones de cada medida
    dict = {} 
    for T in T4:
        if T in dict:
            dict[T]+=1
        else:
            dict[T]=1


    #PRESENTACIÓN DE GRÁFICO
            
    #Se asigna estructura del gráfico mediante la librería matplot
    plt.bar(np.array(getKeys(dict)), np.array(getValues(dict)), width = 0.06, align="center")
    #plt.barh(np.array(getKeys(dict)), np.array(getValues(dict)), height = 0.06, align="center")
    plt.xlabel('Temperatura')
    plt.ylabel('Frecuencia Absoluta')
    plt.title("Gráfico Temperatura Oficina")
    plt.legend(["Temperatura"])
    plt.show()   


def getKeys(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key) 
    return list

def getValues(dict):  
    list = [] 
    for value in dict.values(): 
        list.append(value) 
    return list
    
extraerDatos()
    

