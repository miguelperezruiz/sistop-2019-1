#!/usr/bin/python

import wx
import threading
import time
import os

class Opciones(wx.Frame):
# Todas estas secuencias son para iniciar la ventana donde apareceran las opciones a seleccionar#
  def __init__(self, parent, id, title):
    wx.Frame.__init__(self, parent, id, title, size=(300, 170))

    Opciones = wx.Panel(self, -1)

    self.cb = wx.CheckBox(Opciones, -1, 'DISCO', (10, 10))
    self.cb.SetValue(False)
    wx.EVT_CHECKBOX(self, self.cb.GetId(), self.boolDisk)

    self.cb = wx.CheckBox(Opciones, -1, 'MEMORIA', (120, 10))
    self.cb.SetValue(False)
    wx.EVT_CHECKBOX(self, self.cb.GetId(), self.boolMemory)
    
    self.cb = wx.CheckBox(Opciones, -1, 'PROCESOS', (10, 45))
    self.cb.SetValue(False)
    wx.EVT_CHECKBOX(self, self.cb.GetId(), self.boolProcess)
    
    self.cb = wx.CheckBox(Opciones, -1, 'CPU', (120, 45))
    self.cb.SetValue(False)
    wx.EVT_CHECKBOX(self, self.cb.GetId(), self.boolCpu)

    self.cb = wx.CheckBox(Opciones, -1, 'MarcaParaSeleccionar', (80, 80))
    self.cb.SetValue(False)
    wx.EVT_CHECKBOX(self, self.cb.GetId(), self.boolAux)

    self.Show()
    self.Centre()

# En la sección siguiente se puede saber que opción es seleccionada y mostrarla en la terminal del sistema #

  def boolAux(self, event):
    if self.cb.GetValue():
      print "marcar para seleccionar"

  def boolCpu(self, event):
    if self.cb.GetValue():
      print "CPU"

  def boolProcess(self, event):
    if self.cb.GetValue():
      print "PROCESOS"
      
  def boolDisk(self, event):
    if self.cb.GetValue():
      print "DISCO"
      
  def boolMemory(self, event):
    if self.cb.GetValue():
      print "MEMORIA"


  def disco():
    print ">>>Disco duro<<<\n"

  def memoria():
    print ">>>memoria<<<\n"

  def procesos():
    print ">>>procesos<<<\n"

  def cpu():
    print ">>>cpu<<<\n"

  def ElegirOpcion():
    print ">>>aqui se debe elegir opcion<<<\n"


# Estos se ocupan para hacer uso de la ventana con wxpython #
casillasBooleanas = wx.App()
Opciones(None, -1, 'Opcion a monitorear')
casillasBooleanas.MainLoop()
