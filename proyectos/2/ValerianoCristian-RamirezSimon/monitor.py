#!/usr/bin/python
# coding=utf-8

'''Editor de estilo:'''
#\033[cod_formato;cod_color_texto;cod_color_fondom

from threading import Semaphore, Thread
from time import sleep
import os, threading, time, datetime


mut_impr = threading.Semaphore(1)
band = 0
i=0
j=0

# Definimos la funcion que nos dará a información del uso 
# de disco duro.
def uso_disco():
	'''Impresión de uso de disco'''
	global mut_impr,i,j
	i=1
	j=1
	mut_impr.acquire()
	print("\033[1;37;42m"+"                                        USO DE DISCO                                        "+'\033[0;m\n')
	print " "
	os.system("du -h")
	mut_impr.release()

#Definimos la funcion que imprime el uso de los procesos
def procesos():
	'''Impresión de Procesos'''
	global mut_impr,i,j
	i=1

	mut_impr.acquire()
	j=0
	while j==0:
		print("\033[1;37;42m"+"                                        PROCESOS                                       "+'\033[0;m\n')
		print " "
		os.system("ps -auf")
		print("\033[1;30;47m"+"COMANDOS: memoria(m) | procesos(p) | disco(d) | logins (l) | cpuinfo(c) | interrupts (i) | help(h) | clear (q) | exit(x)"+'\033[0;m')
		mut_impr.release()
		sleep(2)

#Definimos la funcion que imprime el uso de memoria.

def uso_memoria():
	'''Impresión de Uso de Memoria'''
	global mut_impr,i,j
	j=1
	mut_impr.acquire()
	i=0
	while i == 0:

		print("\033[1;37;42m"+"                                        MEMORIA                                        "+'\033[0;m\n')

		os.system("clear")
		now = datetime.datetime.now()

		print (now.strftime("Date: %Y-%m-%d %H:%M:%S"))
		os.system("free -h")
		print "____________________________________________________________________________"
		os.system("cat /proc/meminfo")
		print("\033[1;30;47m"+"COMANDOS: memoria(m) | procesos(p) | disco(d) | logins (l) | cpuinfo(c) | interrupts (i) | help(h) | clear (q) | exit(x)"+'\033[0;m')
		mut_impr.release()
		sleep(2)
	mut_impr.release()		
def logins():
	'''Imprimir Logins'''
	global mut_impr,i,j
	i=1
	j=1
	mut_impr.acquire()
	print("\033[1;37;42m"+"                                        LOGINS                                       "+'\033[0;m\n')
	print " "
	os.system("last")

def cpu_info():
	'''Informacion de CPU'''
	global mut_impr,i,j
	i=1
	j=1
	mut_impr.acquire()
	print("\033[1;37;42m"+"                                        CPU INFO                                        "+'\033[0;m\n')
	print " "
	os.system("cat /proc/uptime")
	os.system("cat /proc/cpuinfo")

def interrupciones():
	'''Impresion de Interrupciones de CPU'''
	global mut_impr,i,j
	i=1
	j=1
	mut_impr.acquire()
	print("\033[1;37;42m"+"                                        INTERRUPCIONES                                        "+'\033[0;m\n')
	print " "
	os.system("cat /proc/interrupts")

def limpia_pantalla():
	'''Limpiar Pantalla'''
	global mut_impr,i,j
	i=1
	j=1
	mut_impr.acquire()
	os.system("clear")

####Función que crea y lanza los hilos cuando son llamados

def command(var):
	'''Lanzador de Hilos'''
	global band

	if var == "d":
		mut_impr.release()
		thr = threading.Thread(target = uso_disco)
		thr.start()
	elif var == "m":
		mut_impr.release()
		thr = threading.Thread(target = uso_memoria)
		thr.start()
	elif var == "p":
		mut_impr.release()
		thr = threading.Thread(target = procesos)
		thr.start()
	elif var == "l":
		mut_impr.release()
		thr = threading.Thread(target = logins)
		thr.start()
	elif var == "c":
		mut_impr.release()
		thr = threading.Thread(target = cpu_info)
		thr.start()
	elif var == "i":
		mut_impr.release()
		thr = threading.Thread(target = interrupciones)
		thr.start()
	elif var == "q":
		mut_impr.release()
		thr = threading.Thread(target = limpia_pantalla)
		thr.start()
	elif var == "h":
		mut_impr.release()
		print '\nEl comando m muestra toda la información de uso de la memoria.\n\nEl comando p muestra la información de cada proceso.\n\nEl comando d despliega el uso total del disco.\n\nEl comando l muestra los logins de sistema.\n\nEl comando c muestra el uso del CPU.\n\nEl comando i muestra las interrupciones del sistema.\n\nEl comando clear limpia la terminal.\n\nEl comando exit finaliza este programa.\n'
		
	elif var == "x":
		global i,j
		i=1
		j=1
		mut_impr.release()

		band = 1
	else:
		print "Invalid command..."
	


def shell():
	'''Funciones en Shell'''
	global var, band, mut_impr
	os.system("clear")
	while band == 0:
#		mut_impr.acquire()
		print("\033[1;30;47m"+"COMANDOS: memoria(m) | procesos(p) | disco(d) | logins (l) | cpuinfo(c) | interrupts (i) | help(h) | clear(q) | exit(x)"+'\033[0;m')
		var = raw_input("user@machine$ ")
		command(var)
		sleep(0.5)
#		mut_impr.release()
				


shell()
