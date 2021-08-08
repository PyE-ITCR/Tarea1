# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv

"""

import numpy as np


input_dir='Utilidades/' #PATH al archivo de datos, cambiar según cada computadora. Sirve para evitar 'File not found'
filename=input_dir+'energydata_complete.csv'

# Esta línea lee la matriz de datos (sin titulos) que van desde T1 hasta RH_9 y funciona para números solamente.
# En su forma actual, esta línea NO LEE datos de tiempo. Para cambios en el mismo, usar la referencia de la funcion genfromtxt como guia
datos=np.genfromtxt(filename,delimiter=';',skip_header=1, usecols = range(3,21))

# Su código va aquí...
