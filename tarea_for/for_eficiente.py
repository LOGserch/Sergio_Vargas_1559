
a = 12
"""imprime la multiplicacion del valor asignado a "a",pero el valor es estatico en el 
   transcurso del programa hasta que se cambie el valor en el termino del mismo
   por lo tanto es eficiente por "multiplicar correctamente" , pero no eficaz
"""
for i in range(1, 11):
    for x in range(1, 11):

        print(i, " x ", x, " = ", (i*x))

    print("-"*30)