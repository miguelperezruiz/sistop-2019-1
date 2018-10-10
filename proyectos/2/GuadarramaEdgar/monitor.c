//Monitor de Sistema 
//Guadarrama Flores Edgar Alejandro
//
#include <unistd.h>
#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gtk/gtk.h>
 
FILE *fp;
 
struct datosProceso {
    char nombre[32];
    char estado[8];
    int nThreads;
    int tamanioMemoria;
};
 
struct datosSistema {
    int hilosCorriendo;
    int totalSubprocesos;
    float promedioCPU[4];//uso del sistema en promedio de 1 seg y de 1, 5 y 10 minutos
    int ultimoPIDEjecutado;
    char modeloCPU[128];
    int nNucleosVirtuales;
    int nNucleosFisicos;
    char memoriaTotal[64];
    char memoriaLibre[64];
} sistema;
 
struct datosProceso inspeccionarProcesoID(int pid)//obtiene el nombre, estado, numero de subprocesos y memoria usada por el proceso pid
{
    struct datosProceso tmp;
    tmp.nombre[0]=0;
    tmp.estado[0]=0;
    tmp.nThreads=0;
    tmp.tamanioMemoria=0;
    char sFile[64];
    sprintf(sFile, "/proc/%i/stat", pid);
    if(access(sFile, F_OK) != -1)
    {
        fp = fopen(sFile,"r");
        fscanf(fp,"%*s %s %s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %*s %i",tmp.nombre, tmp.estado, &tmp.nThreads);
        fclose(fp);
    }
    sprintf(sFile, "/proc/%i/statm", pid);
    if(access(sFile, F_OK) != -1)
    {
        fp = fopen(sFile,"r");
        fscanf(fp,"%i",&tmp.tamanioMemoria);
        fclose(fp);
    }
    return tmp;
}
