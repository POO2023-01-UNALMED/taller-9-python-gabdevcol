import tkinter
from asyncio import events
from tkinter import *




# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x250")

# Configuración pantalla de salida
variable_pantalla = StringVar()
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"), textvariable=variable_pantalla)
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# def pulsarBotonInt(numero):
#     print(numero)


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)


class Calcular:

    n1 = -1
    n2 = -1
    op = ""

    @classmethod
    def setn1(cls, valor):
        cls.n1 = valor

    @classmethod
    def setn2(cls, valor):
        cls.n2 = valor

    @classmethod
    def setop(cls, valor):
        cls.op = valor

calcular = Calcular

def pulsarBotonInt(numero):
    if calcular.n1 <0:
        calcular.setn1(numero)
    else:
        calcular.setn2(numero)
    variable_pantalla.set(str(numero))

def pulsarMas():
    if calcular.n1 > -1:
        calcular.setop("+")
        variable_pantalla.set("+")
    else:
        variable_pantalla.set("escoja un numero")

def pulsarMenos():
    if calcular.n1>-1:
        calcular.setop("-")
        variable_pantalla.set("-")
    else:
        variable_pantalla.set("escoja un numero")

def pulsarPor():
    if calcular.n1 > -1:
        calcular.setop("*")
        variable_pantalla.set("*")

    else:
        variable_pantalla.set("escoja un numero")

def pulsarDivision():
    if calcular.n1 > -1:
        calcular.setop("/")
        variable_pantalla.set("/")
    else:
        variable_pantalla.set("escoja un numero")

def pulsarIgual():
    n1= calcular.n1
    n2 = calcular.n2
    print(n1,n2)
    resultado = 0
    if n1>-1 and n2>-1 and calcular.op !="":
        if calcular.op == "+":
            resultado = n1+n2
            variable_pantalla.set(str(resultado))
        elif calcular.op == "-":
            resultado = n1 - n2
            variable_pantalla.set(str(resultado))
        elif calcular.op == "*":
            resultado = n1 * n2
            variable_pantalla.set(str(resultado))
        else:
            resultado = n1 / n2
            variable_pantalla.set(str(resultado))

    else:
        variable_pantalla.set("defina una operacion")
    calcular.setn1(-1)
    calcular.setn2(-1)
    calcular.setop("")


boton_1.bind('<Button-1>', lambda event , numero = 1: pulsarBotonInt(numero))
boton_2.bind('<Button-1>', lambda event , numero = 2: pulsarBotonInt(numero))
boton_3.bind('<Button-1>', lambda event , numero = 3: pulsarBotonInt(numero))
boton_4.bind('<Button-1>', lambda event , numero = 4: pulsarBotonInt(numero))
boton_5.bind('<Button-1>', lambda event , numero = 5: pulsarBotonInt(numero))
boton_6.bind('<Button-1>', lambda event , numero = 6: pulsarBotonInt(numero))
boton_7.bind('<Button-1>', lambda event , numero = 7: pulsarBotonInt(numero))
boton_8.bind('<Button-1>', lambda event , numero = 8: pulsarBotonInt(numero))
boton_9.bind('<Button-1>', lambda event , numero = 9: pulsarBotonInt(numero))
boton_mas.bind('<Button-1>', lambda event : pulsarMas())
boton_menos.bind('<Button-1>', lambda event : pulsarMenos())
boton_multiplicacion.bind('<Button-1>', lambda event : pulsarPor())
boton_division.bind('<Button-1>', lambda event : pulsarDivision())
boton_igual.bind('<Button-1>', lambda event : pulsarIgual())





root.mainloop()

