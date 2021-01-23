def Octal(dec):
if dec > 0:
 Octal((int)(dec/8))
 print(dec%8, end='')


decimal=int(input("escoge un numero a convertir: "))
print(Octal(decimal))
	
