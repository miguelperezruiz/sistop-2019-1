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
#desplegando informcaion del uso de CPU
def use_CPU():
	global semaforo
	semaforo.acquire()	
	file = open("/proc/loadavg")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
#desplegando informacion de las particiones de Disco
def disk_part():
	global semaforo
	semaforo.acquire()	
	file = open("/proc/mounts")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
#desplegando informacion de los ultimos procesos ejecutados
def process_act():
	global semaforo
	semaforo.acquire()
	os.system("ps -l"); #mostramos los mas recientes en formato largo
	semaforo.release();
#desplegando informacion del uso de memoria
def mem_st():
	global semaforo
	semaforo.acquire()
	os.system("free -h"); #mostramos espacio en memoria en formato Humano :V
						  #eso quiere decir: escalado para que sea entendible
	semaforo.release();
#desplegando informacion sobre los sistemas de archivos soportados por el OS
def fileSys_info():
	global semaforo
	semaforo.acquire()	
	file = open("/proc/filesystems")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
#desplegando informacion de ayuda para el manejo del monitor
def info():
	global semaforo
	semaforo.acquire()	
	file = open("info.txt")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
#desplegando informacion sobre los desarrolladores
def acerca_de():
	global semaforo
	semaforo.acquire()	
	file = open("proyecto.txt")
	lectura = file.readline()
	while lectura != "":
		print lectura
		lectura = file.readline()
	file.close()
	semaforo.release()
