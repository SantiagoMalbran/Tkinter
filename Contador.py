from tkinter import *
from threading import Thread
import time
import tkinter

contador=True
limit=100
limit2=0


def click_up():
   global contador
   contador=False
   while not contador and int(inicio.get())<=limit:
       time.sleep (0.1)
       inicio.set(str(int(inicio.get())+1))
def contador(e):
    global contador
    contador=True

def click_Down():
   global contador
   contador=False
   while not contador and int(inicio.get())>=limit2:
       time.sleep (0.2)
       inicio.set(str(int(inicio.get())-1))
def contador(e):
    global contador
    contador=True

def click_Reset():
    inicio.set(0)



ventanaContador=tkinter.Tk()
ventanaContador.geometry("600x300")

Econtador=tkinter.Label(text="contador")
Econtador.grid(row=0,column=0)
inicio=tkinter.StringVar()
valor=tkinter.Entry(ventanaContador,state="disable",bg="green",textvariable=inicio)
valor.grid(row=0,column=1)
inicio.set("0")
up=tkinter.Button(ventanaContador,text="Count UP")
up.bind('<Button-1>', lambda e: Thread(target=click_up, daemon=True).start())
up.bind('<ButtonRelease-1>', contador)
up.grid(row=0,column=2)
down=tkinter.Button(ventanaContador,text="Count Down")
down.bind('<Button-1>', lambda e: Thread(target=click_Down, daemon=True).start())
down.bind('<ButtonRelease-1>',contador)
down.grid(row=0,column=3)
Breset=tkinter.Button(ventanaContador,text="Reset")
Breset.bind('<Button-1>', lambda e: Thread(target=click_Reset, daemon=True).start())
Breset.grid(row=0,column=4)


ventanaContador.mainloop()
