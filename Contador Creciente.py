from tkinter import *
from threading import Thread
import time
import tkinter

contador=True
limit=100





ventana=tkinter.Tk()
ventana.geometry("300x300")

def click():
   global contador
   contador=False
   while not contador and int(inicio.get())<limit:
       time.sleep (0.1)
       inicio.set(str(int(inicio.get())+1))
def contador(e):
    global contador
    contador=True
        

etiquetaC=tkinter.Label(ventana, text="contador",bg="red")
etiquetaC.grid(row=0,column=0)
inicio=tkinter.StringVar()
etiqueta2=tkinter.Label(ventana,textvariable=inicio)
etiqueta2.grid(row=0,column=1)
inicio.set("18")
boton=tkinter.Button(ventana,text="+")
boton.bind('<Button-1>', lambda e: Thread(target=click, daemon=True).start())
boton.bind('<ButtonRelease-1>', contador)
boton.grid(row=0,column=2)






    






ventana.mainloop()