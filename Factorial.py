from threading import Thread
from tkinter import *
import tkinter

contador = 0

def factorial():
    global contador
    if int(numaux)+contador == 1:
        contador+=1
        return resultado.set(1)
    else:
        numfactorial.set(contador+1)
        res = 1
        for i in range(1,int(numaux)+1+contador):
            res*=i
        contador+=1
        return resultado.set(res)


ventanafactorial=tkinter.Tk()
ventanafactorial.geometry("600x300")

valor1=tkinter.Label(ventanafactorial,text="n")
valor1.grid(row=0,column=0)

numfactorial = IntVar()
numfactorial.set("1")
numerofactorial=tkinter.Entry(ventanafactorial,state="disable",textvariable=numfactorial)
numerofactorial.grid(row=0,column=1)
numaux = numerofactorial.get()

valor2=tkinter.Label(ventanafactorial,text="Factorial(n)")
valor2.grid(row=0,column=2)

resultado=IntVar()
numero=tkinter.Entry(ventanafactorial,state="disable",textvariable=resultado)
numero.grid(row=0,column=3)
resultado.set("")

siguiente=tkinter.Button(ventanafactorial,text="Siguiente")
siguiente.bind('<Button-1>', lambda e: Thread(target=factorial, daemon=True).start())
siguiente.bind('<ButtonRelease-1>', contador)
siguiente.grid(row=0,column=4)






ventanafactorial.mainloop()





