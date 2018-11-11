#!/usr/bin/python3
#Sanchez Espinosa Andrew Blaise
#Proyecto 3 (micro) Sistema de Archivos.

import os

def mst(cmd):
	print("Debe mostrar el archivo")
def brr(cmd):
	print("Debe borrar el archivo")
def lsdoc(cmd):
	print("Debe mostrar el directorio de archivos")
def crr(cmd):
	print("Debe crear el archivo")
def agg(cmd):
	print("Debe agregar informacion al archivo")
def ayuda(cmd):
	print("AYUDA!!")

def main():
	print("\n\t Bienvenido (Micro) sistema de archivos BlaiseSe.")
	print("\t -- Escriba ayuda para ayuda ")
	print("\t -- Escriba lsdoc para mostrar los archivos en el directorio ")
	print("\t -- Escriba brr para borrar ")
	print("\t -- Escriba mst para mostrar el contenido de un archivo ")
	print("\t -- Escriba crr para crear un archivo ")
	print("\t -- Escriba agg para agregar informacion a un archivo ya creado ")
	print("\t -- Escriba yapara para cerrar el (micro) Sistema de Archivos ")

	cmd =raw_input("~$:  ").split(" ")
	lscmd={"lsdoc":lsdoc,"brr":brr,"mst":mst,"ayuda":ayuda,"crr":crr,"agg":agg}
	while cmd[0] != "yapara":
		try:
			func=lscmd[cmd[0]]
			if len(cmd)>3:	
				aux=""
				for i in range(2,len(cmd)):
					aux+=cmd[i]+" "
				cmd=[cmd[0],cmd[1],aux]
			func(cmd)
		except KeyError:
			print("error 404 -.-' ")
		cmd=raw_input("~$: ").split(" ")

main()
