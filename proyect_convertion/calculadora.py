from tkinter import *

raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

operacion = ""  # def var para operaciones aritmeticas

resultado = 0  # def variable para resultados aritmeticos

# ---------------------------------------------------------------
numPantalla = StringVar()  # recibe un valor "string"

# pantalla principal o de visualizacion de datos
pantalla = Entry(miFrame, textvariable=numPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


# ----------------------------------------------------------------

def numeroPulsado(num):
    global operacion

    if operacion != "":
        numPantalla.set(num)  # mostrar num en pantalla
        operacion = ""
    else:
        numPantalla.set(numPantalla.get() + num)  # set establece un valor en pantalla


# ------------------funcion suma----------------------------------

def suma(num):
    global operacion
    global resultado
    resultado += int(num)

    operacion = "suma"
    numPantalla.set(resultado)


# ------------------funcion suma----------------------------------

def resta(num):
    global operacion
    global resultado
    resultado = int(num) - resultado

    operacion = "resta"
    numPantalla.set(resultado)


# ------------------funcion suma----------------------------------

def mult(num):
    global operacion
    global resultado
    resultado = int(num) * resultado

    operacion = "mult"
    numPantalla.set(resultado)


# ------------------funcion suma----------------------------------

def div(num):
    global operacion
    global resultado
    resultado = int(num) / resultado

    operacion = "div"
    numPantalla.set(resultado)


# ------------------funcion suma----------------------------------

def ra(num):
    global operacion
    global resultado
    resultado += int(num)

    operacion = "ra"
    numPantalla.set(resultado)


# ------------------------funcion el_resultado----------------------------------------
def el_resultado():
    global resultado

    numPantalla.set(resultado - int(numPantalla.get()))
    resultado = 0


# ----------------------------------------------------------------
buttonDel = Button(miFrame, text="DEL", width=3, command=lambda: numeroPulsado("7"))
buttonDel.grid(row=2, column=1)
buttonDo = Button(miFrame, text="C", width=3, command=lambda: numeroPulsado(""))
buttonDo.grid(row=2, column=2)
buttonRaiz = Button(miFrame, text="Raiz", width=3, command=lambda: numeroPulsado(""))
buttonRaiz.grid(row=2, column=3)
buttonExponente = Button(miFrame, text="^", width=3, command=lambda: ra(numPantalla.get()))
buttonExponente.grid(row=2, column=4)

# ----------------------------------------------------------------
button7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
button7.grid(row=3, column=1)
button8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
button8.grid(row=3, column=2)
button9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
button9.grid(row=3, column=3)
buttonM = Button(miFrame, text="X", width=3, command=lambda: mult(numPantalla.get()))
buttonM.grid(row=3, column=4)

# ----------------------------------------------------------------

button4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
button4.grid(row=4, column=1)
button5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
button5.grid(row=4, column=2)
button6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
button6.grid(row=4, column=3)
buttonR = Button(miFrame, text="-", width=3, command=lambda: resta(numPantalla.get()))
buttonR.grid(row=4, column=4)

# ----------------------------------------------------------------

button1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
button1.grid(row=5, column=1)
button2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
button2.grid(row=5, column=2)
button3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
button3.grid(row=5, column=3)
buttonMAS = Button(miFrame, text="+", width=3, command=lambda: suma(numPantalla.get()))
buttonMAS.grid(row=5, column=4)

# ----------------------------------------------------------------

buttonPunto = Button(miFrame, text=".", width=3, command=lambda: numeroPulsado("."))
buttonPunto.grid(row=6, column=1)
button0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
button0.grid(row=6, column=2)
buttonDiv = Button(miFrame, text="/", width=3, command=lambda: div(numPantalla.get()))
buttonDiv.grid(row=6, column=3)
buttonE = Button(miFrame, text="=", width=3, command=lambda: el_resultado())
buttonE.grid(row=6, column=4)
raiz.mainloop()
