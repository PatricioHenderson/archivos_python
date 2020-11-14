#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Patricio Henderson"
__email__ = "patriciohenderson@hotmail.com"
__version__ = "1.3"

import re
import csv
def ironman():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
def multiplicador (deporte):
    
    try:

        deporte = str(deporte)
        deporte = deporte.split(":")
        deporte = int(deporte[0])*3600+int(deporte[1])*60+ (int(deporte[2]))
        return deporte
    
    except:
        pass


with open ("Ironman.csv") as fo:
        
        archivo = list(csv.DictReader(fo))
        len_reader = len(archivo)
        #Abrimos el archivo y sacamos el largo
        cantidad_corredores_mpro = 0
        mas_swim_mpro = 0
        mas_bike_mpro = 0
        mas_run_mpro = 0
        

    
        for i in range(len_reader):
            #iteramos todo el archivo

            linea = archivo[i]
            division = linea.get("Division")
            swim = linea.get("Swim")
            bike = linea.get("Bike")
            run = linea.get("Run") 

            segundos_swim = multiplicador(swim)
            segundos_bike = multiplicador(bike)
            segundos_run = multiplicador(run)

            if division == "MPRO"  :
                try :
                    
                    


                    cantidad_corredores_mpro += 1
                    #Contamos cantidad de corredores MPRO y los almacenamos 

                    if mas_swim_mpro is None or segundos_swim > mas_swim_mpro:
                        mas_swim_mpro = segundos_swim 
                    #Buscamos al que mas tiempo nado


                    if mas_bike_mpro is None or segundos_bike > mas_bike_mpro:
                        mas_bike_mpro = segundos_bike
                    #buscamos al que más tiempo pedaleo

            
                    if mas_run_mpro is None or segundos_run > mas_run_mpro:
                        mas_run_mpro = segundos_run
                    #Buscamos al que más tiempo  corrio
                except:
                    pass
            
        print(mas_swim_mpro, mas_bike_mpro, mas_run_mpro)
               
              


if __name__ == '__main__':
    print("Ejercicios de práctica extra")
    
    ironman()
    
