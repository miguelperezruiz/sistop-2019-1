import os,threading, time
from threading import Semaphore,Thread

#seccion Critica: variable global que sera utilizada por
#todos los Hilos de mi proceso principal
semaforo = threading.Semaphore()	#un solo hilo puede entrar a zona critica

"""
 Todo el bloque siguiente representa a los comandos
soportados por el monitor. Dichas funciones estaran
asociadas a los hilos que seran sincronizados por el
semaforo.
"""
#desplegando informacion del CPU de la Computadora anfitriona
def CPU_info():
	global semaforo
	semaforo.acquire()	
	file = open("/proc/cpuinfo")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
#desplegando informacion de la memoria de la Computadora anfitriona
def memory_info():
	global semaforo
	semaforo.acquire()	
	file = open("/proc/meminfo")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
#desplegando informacion del tiempo de uso del cpu
def use_time():
	global semaforo
	semaforo.acquire()	
	file = open("/proc/uptime")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
