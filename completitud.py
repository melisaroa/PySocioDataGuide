# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:26:54 2023

@author: Melisa
"""
# Librerias
import pandas as pd

# Directorio 
%cd "F:\direccion de donde se guarda la base de datos"


# Base de datos a utilizar
datos = pd.read_excel("2005_2023_ingreso_tipodeempleo_entidad.xlsx", sheet_name= "Tabulado")

# Defines la función
def calcular_porcentaje_nan(dataframe):
    total_valores = dataframe.size
    valores_nan = dataframe.isnull().sum().sum()
    porcentaje_nan = (valores_nan / total_valores) * 100
    porcentaje_completo = 100 - porcentaje_nan
    return porcentaje_completo

# Aplicas la función
porcentaje_completo = calcular_porcentaje_nan(datos)
print(f"El porcentaje de completitud de los datos es: {porcentaje_completo}%")
