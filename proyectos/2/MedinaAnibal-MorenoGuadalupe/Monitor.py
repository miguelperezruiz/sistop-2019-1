#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import subprocess
import time
import sys
import threading
import psutil

# Numero de nucleos que tiene nuestra computadora
NumNucleos = int(subprocess.getoutput("grep processor /proc/cpuinfo | wc -l"))

# Mutex para proteger al contador
mutex = threading.Semaphore(1)
aviso = threading.Semaphore(1)
global contahilos
contahilos = 0

# Semáforo para señalizar que todos los hilos cumplieron con su funcion
signal = threading.Semaphore(0)



# señalizar entre hilos
def alertProces():
	# Adquirimos el mutex para escritura y lectura de la variable contador de hilos
	aviso.acquire()
	global contahilos
	contahilos += 1
	if contahilos == func_monitor:
		signal.release()
	# Se libera mutex
	aviso.release()



# Se da el modelo del CPU de la computadora donde se corra el programa
def modeloCPU():
    # Guardamos lo que haya en /proc/cpuinfo y filtramos el apartado donde diga el modelo
    modelo = subprocess.getoutput("cat /proc/cpuinfo | grep -e 'model\ name'")
    modeloFiltro = ""
    for i in modelo:
        if i == '\n':
            modeloFiltro = modeloFiltro.replace("model name\t: ","")
            return modeloFiltro
        modeloFiltro += i

# obtener el kernel del SO
def kernel():
    version_so = subprocess.getoutput("cat /proc/version | while read c1 c2 c3 c4; do echo $c1 $c2 $c3; done")
    return version_so



#saber el porcentaje de uso del cpu que está manejando el Usuario
def Usuario():
    cpu1 = subprocess.getoutput("cat /proc/stat | grep 'cpu ' | while read c1 c2 c3; do echo $c2; done")
    time.sleep(1)
    cpu2 = subprocess.getoutput("cat /proc/stat | grep 'cpu ' | while read c1 c2 c3; do echo $c2; done")
    # calculamos el tiempo tomando dos muestreos con un segundo de diferencia y se divide entre el número de nucleos
    cpu_uso = (int(cpu2) - int(cpu1)) / numNucleos
    alertProces()
    return str(cpu_uso)

# saber el porcentaje de uso del cpu que está manejando el Sistema
def Sistema():
    estado1 = subprocess.getoutput("cat /proc/stat | grep 'cpu ' | while read c1 c2 c3 c4 c5; do echo $c4; done")
    time.sleep(1)
    estado2 = subprocess.getoutput("cat /proc/stat | grep 'cpu ' | while read c1 c2 c3 c4 c5; do echo $c4; done")
    cpu_uso = (int(estado2) - int(estado1)) / NumNucleos
    alertProces()
    return str(cpu_uso)

# saber el porcentaje de uso que está Inactivo
def cpuInactivo():
    estado1 = subprocess.getoutput("cat /proc/stat | grep 'cpu ' | while read c1 c2 c3 c4 c5 c6; do echo $c5; done")
    time.sleep(1)
    estado2 = subprocess.getoutput("cat /proc/stat | grep 'cpu ' | while read c1 c2 c3 c4 c5 c6; do echo $c5; done")
    cpu_uso = (int(estado2) - int(estado1)) / NumNucleos
    alertProces()
    return str(cpu_uso)



# memoria total que tiene nuestra computadora, se muestra en kB
def MemoTotal():
    memtotal =  subprocess.getoutput("cat /proc/meminfo | while read c1 c2; do echo $c2; done | sed -n '1 p'")
    alertProces()
    return memtotal

# memoria libre que tiene nuestra computadora( se muestra en kB)
def MemoLibre():
    memlibre =  subprocess.getoutput("cat /proc/meminfo | while read c1 c2; do echo $c2; done | sed -n '2 p'")
    alertProces()
    return memlibre

# memoria que está usando el usuario(se muestra en kB)
def MemoUso():
    memuso =  subprocess.getoutput("cat /proc/meminfo | while read c1 c2; do echo $c2; done | sed -n '7 p'")
    alertProcess()
    return memuso

