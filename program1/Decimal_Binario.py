
# Function to print binary number using recursion

def Binario(n):

   if n > 1:

       Binario(n//2)

   print(n % 2,end = '')


# decimal number

dec = int(input("agregue el numero a convertir: "))


Binario(dec)

print()
