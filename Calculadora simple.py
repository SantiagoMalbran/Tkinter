from tkinter import *
from threading import Thread
import time
import tkinter



ventanaCalc=tkinter.Tk()
ventanaCalc.geometry("300x600")

def click_suma():
    res = int(primernumero.get())+int(segundonumero.get())
    return resultado2.set(res)

def click_resta():
    res = int(primernumero.get())-int(segundonumero.get())
    return resultado2.set(res)

def click_multiplicacion():
    res = int(primernumero.get())*int(segundonumero.get())
    return resultado2.set(res)

def click_division():
    res = int(primernumero.get())/int(segundonumero.get())
    return resultado2.set(res)

def click_modulo():
    res = int(primernumero.get())%int(segundonumero.get())
    return resultado2.set(res)
    
def click_clear():
    dato1.set("")
    dato2.set("")
    resultado2.set("")

dato1=IntVar()
etiqueta1=tkinter.Label(ventanaCalc,text="Primer numero")
etiqueta1.grid(row=0,column=0)

primernumero=tkinter.Entry(ventanaCalc,textvariable=dato1)
primernumero.grid(row=0,column=1)
dato1.set("")


dato2=IntVar()
etiqueta2=tkinter.Label(ventanaCalc,text="Segundo numero")
etiqueta2.grid(row=1,column=0)

segundonumero=tkinter.Entry(ventanaCalc,textvariable=dato2)
segundonumero.grid(row=1,column=1)
dato2.set("")

etiqueta3=tkinter.Label(ventanaCalc,text="Resultado")
etiqueta3.grid(row=2,column=0)


resultado2=tkinter.StringVar()
resultado=tkinter.Entry(ventanaCalc,state="disable",textvariable=resultado2)
resultado.grid(row=2,column=1)
resultado2.set("")



botonmas=tkinter.Button(ventanaCalc,text="+",command=click_suma)
# botonmas.bind('<Button-1>', lambda e: Thread(target=click_suma, daemon=True).start())
botonmas.grid(row=3,column=0,ipadx=50,ipady=5)

botonmenos=tkinter.Button(ventanaCalc,text="-",command=click_resta)
botonmenos.grid(row=3,column=1,ipadx=50,ipady=5)

botonx=tkinter.Button(ventanaCalc,text="*",command=click_multiplicacion)
botonx.grid(row=4,column=0,ipadx=50,ipady=5)

botondiv=tkinter.Button(ventanaCalc,text=(u"\u00F7"),command=click_division)
botondiv.grid(row=4,column=1,ipadx=50,ipady=5)

botonprocentaje=tkinter.Button(ventanaCalc,text="%",command=click_modulo)
botonprocentaje.grid(row=5,column=0,ipadx=50,ipady=5)

botonCE=tkinter.Button(ventanaCalc,text="CE",command=click_clear)
botonCE.grid(row=5,column=1,ipadx=50,ipady=5)







ventanaCalc.mainloop()