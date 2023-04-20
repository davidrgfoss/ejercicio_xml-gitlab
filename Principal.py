#!/usr/bin/env python3

from lxml import etree
from Funciones import *
from os import system
doc = etree.parse('Libros.xml')

while True:
    system("clear")
    print ("Menu principal")
    print ("-"*55)
    print ("1. Listar informacíon.")
    print ("2. Contar Información.")
    print ("3. Buscar o filtrar información.")
    print ("4. Buscar informacion relacionada.")
    print ("5. Ejercicio libre.")
    print ("6. Salir del programa.")
    opcion=int(input("Opcion: "))
    if opcion == 1:
        system("clear")
        print ("Titulos de los libros")
        print ("-"*55)
        for x in ListarInformacion(doc):
            print ("La descripcion del titulo ----%s---- es:" %(x[0]))
            print (x[1])
            print()
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 2:
        system("clear")
        print ("Contar cantidad de libro segun su genero")
        print ("-"*55)
        cad=input("Introduce un genero> ").capitalize()
        print ("Hay un total de %s libros con ese genero." %(ContarInformacion(doc,cad)))
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 3:
        system("clear")
        print ("Mostrar los libros que estan en un rango de precio")
        print ("-"*55)
        count=1
        cad=input("Introduce un precio> ")
        cad1=input("Introduce otro precio> ")
        for x in FiltrarInformacion(doc,cad,cad1):
            print ("Libro %i: %s." %(count,x))
            count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 4:
        system("clear")
        print ("Buscar los libros segun el subgenero que tiene")
        print ("-"*55)
        count=1
        cad=input("Introduce un subgenero> ").capitalize()
        for x in BuscarInformacion(doc,cad):
            print ("Libro %i: %s." %(count,x))
            count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 5:
        system("clear")
        print ("Mostrar libros en un rango de fecha")
        print ("-"*55)
        print ("Debes introducir dos fechas con el formanto 'DD/MM/YYYY'")
        fecha1=input("Fecha 1: ").split("/")
        fecha1[::-1]=[int(x) for x in fecha1]
        fecha2=input("Fecha 2: ").split("/")
        fecha2[::-1]=[int(x) for x in fecha2]
        count=1
        for x in Calcularfecha(doc,fecha1,fecha2):
            for f in Ejerciciolibre(doc,x):
                print ("Libro %i: %s con el genero principal %s." %(count,f[0],f[1]))
                count+=1
        print ("-"*55)
        input("Pulsa intro para continuar.")
    elif opcion == 6:
        system("clear")
        break
    else:
        system("clear")
print ("Fin del programa")