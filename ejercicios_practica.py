#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Patricio Henderson"
__email__ = "patriciohenderson@hotmail.com"
__version__ = "1.3"

import csv
import re
def contar_lineas (archivo):
        fo = open(archivo , "r")
        contenido_completo = fo.read()
        cantidad_lineas = 0
        for i in contenido_completo:
            if i == "\n":
                cantidad_lineas += 1
        fo.close
        print (cantidad_lineas , "mediante función")

def ej1():
    # Ejercicios con archivos txt
    
    """def contar_lineas (documento):
        fo = open(documento,"r")
        contenido_completo = fo.read()
        for i in contenido_completo:
            if i == "\n":
                cantidad_lineas += 1
        fo.close()
    print(cantidad_lineas)
    """
    def contar_lineas (archivo):
        fo = open(archivo , "r")
        contenido_completo = fo.read()
        cantidad_lineas = 0
        for i in contenido_completo:
            if i == "\n":
                cantidad_lineas += 1
        fo.close
        print (cantidad_lineas , "mediante función")
    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    fo = open("notas.txt" , "r")
    contenido_completo = fo.read()
    cantidad_lineas = contenido_completo.count("\n")
    fo.close()
    print(cantidad_lineas)
    
    contar_lineas("notas.txt" )

    with open ("notas.txt") as archivo_completo:
        archivo_completo = archivo_completo.read()
        lineas =0
        for i in archivo_completo:
            if i == "\n":
                lineas =+ 1
    print(lineas)

def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''
    fi = open("notas.txt" , "r")
    fo = open ("copia.txt" , "w")
    
    lectura = fi.read()
    lineas = lectura.count("\n")
    escritura = fo.write(lectura)

    print("Se copiaron {} lineas de texto." .format(lineas))

    fi.close()
    fo.close()
    contar_lineas("copia.txt")

    # Recuerde cerrar los archivos al final ;)


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    with open ("propiedades.csv") as csvfile:
        
        archivo = list(csv.DictReader(csvfile))
        cantidad_deptos = 0
        for i in archivo:
            if (i["ambientes"]) == "2" or (i["ambientes"] =="3") :
                cantidad_deptos += 1
        print(cantidad_deptos)
        
        

def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    '''
    print("Ingrese Fin para terminar el programa: ")
    
    while True:
        fruta = str(input("Item : "))
        #Solicitar ingreso manual del item a agregar
        if fruta == "fin":
            break
        cantidad= int(input("Cantidad: "))
        #Solicitar ingreso manual de la cantidad de items a agregar
        if cantidad == "fin":
            break
        
        inventario[fruta.strip()] = cantidad.strip()
        #Añadimos al diccionario eliminado espacios al final

    print(inventario)

    item_buscado = str(input("Introducir producto a buscar: "))
    item_buscado = item_buscado.strip()

    print("Hay {} {}".format(inventario[item_buscado],item_buscado))


    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"


def ej5():
    # Ejercicios con archivos CSV
    inventario = {'Fruta Verdura': 'manzana', 'Cantidad': 10}

    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''

    with open("ej5.csv","w", newline="") as fo:
        header = ["Fruta Verdura","Cantidad"]
        
        writer = csv.DictWriter (fo, fieldnames = header)
        writer.writeheader()
        
        #Crea el archivo con las claves
        while True:
            item = str(input("Introducir fruta o verdura :"))
            if item == "fin":
                break
            cantidad= int(input("Cantidad: "))
            #Solicitar ingreso manual de la cantidad de items a agregar
            if cantidad == "fin":
                break
            
            inventario[item] = cantidad

            writer.writerow({'Fruta Verdura': item, 'Cantidad': cantidad})

        
   

        
        


    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
