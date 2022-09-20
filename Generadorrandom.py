from pydoc import text
from random import randint
from tkinter import *
import tkinter


def random():

    numero = randint(int(primernumero.get()),int(segundonumero.get()))
    return resultado2.set(numero)

ventanarandom=tkinter.Tk()
ventanarandom.geometry("300x600")
ventanarandom.title("generador")

etiqueta1=tkinter.Label(ventanarandom,text="Número 1")
etiqueta1.grid(row=0,column=0)
dato1=IntVar()
primernumero=tkinter.Entry(ventanarandom)
primernumero.grid(row=0,column=1)




etiqueta2=tkinter.Label(ventanarandom,text="Número 2")
etiqueta2.grid(row=1,column=0)
segundonumero=tkinter.Entry(ventanarandom)
segundonumero.grid(row=1,column=1)


etiqueta3=tkinter.Label(ventanarandom,text="Número generado")
etiqueta3.grid(row=2,column=0)

resultado2=StringVar()
resultado=tkinter.Entry(ventanarandom,state="disable",textvariable=resultado2)
resultado.grid(row=2,column=1)

generador= tkinter.Button(ventanarandom,text="Generar",command=random)
generador.grid(row=3,column=1)

ventanarandom.mainloop()