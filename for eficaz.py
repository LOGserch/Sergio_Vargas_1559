m = int(input("que multiplicacion desea?(-1 para terminar) "))

"""
el programa ocupa mas lineas de codigo y mas estructuras de control que el programa eficiente,pero
la ventaja mas obvia de este programa es que es eficaz al momento de poder hacer todo tipo de
multiplicaciones sencillas en una sola ejecucion sin necesitad de cambiar la variable cada vez que se
para el programaademas de tener la opcion de terminar su ejecucion si el usuario asi lo desea(con -1
que esta especificado en la entrada de datos)
"""
while m != -1:
    contador = 1
    for i in range(1, 11):

        print(m, " x ", contador, " = ", (m*contador))
        contador += 1

    print("-"*30)

    m = int(input("que multiplicacion desea?(-1 para terminar) "))

print("programa terminado con exito")