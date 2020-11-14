#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Patricio Henderson"
__email__ = "patriciohenderson@hotmail.com"
__version__ = "1.4"
import csv
import re
import statistics

def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    with open ("texto.txt", "r") as fo :

        fo = fo.read()
        for i in fo:
            cantidad_letras += 1
        print(cantidad_letras)
    
    fo = open("texto.txt","r")
    for i in fo:
        cantidad_letras += len(i)
    fo.close()
    print(cantidad_letras)
def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    with open ("ej2_prof.txt" , "w") as fo:

        while True:
            texto = str(input("Introducir texto : ")) + "\n"
            for i in texto :
                cantidad_letras += 1
            fo.write(texto)
            if texto == "" + "\n":
                break




def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = "2"

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    cantidad_ambientes = str(input("Departamento de cuantos ambientes busca: "))
    with open ("propiedades.csv") as fo:
        
        deptos = 0
        suma_precio = 0
        menor_valor = None
        mayor_valor= None
        archivo = list(csv.DictReader(fo))
        len_reader = len(archivo)

        
        for i in range(len_reader):
            linea = archivo[i]

            precio = linea.get("precio")
            moneda = linea.get("moneda")
            ambientes = linea.get("ambientes")

            if ambientes == cantidad_ambientes and moneda == "ARS":
                deptos += 1
                suma_precio += float(precio)

                if menor_valor is None or menor_valor > float(precio):
                    menor_valor = float(precio)

                if mayor_valor is None or mayor_valor < float(precio):
                    mayor_valor= float(precio)
               
        print ("Hay {} departamentos de {} ambientes" .format(deptos,cantidad_ambientes))
        print("precio promedio", suma_precio / deptos ,"\n",
        "Mas barato : ", menor_valor,"\n""Mas Caro", mayor_valor)
        
        



if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
