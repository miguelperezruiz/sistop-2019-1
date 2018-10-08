import wx

class Opciones(wx.Frame):
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

casillasBooleanas = wx.App()
Opciones(None, -1, 'Opcion a monitorear')
casillasBooleanas.MainLoop()
