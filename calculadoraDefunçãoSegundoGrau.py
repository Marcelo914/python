import math
from re import A, X
from this import d
from tkinter import Y

A =int(input("valor de A: "))
B = int(input("valor de B: "))
C = int(input("valor de C: "))

delta = B**2 - 4 * A * C
if delta== 0:
    X = (-B + math.sqrt(delta)) /(A*2)
    print("A raiz dessa equação é: ", X)
else: 
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
         x1 = (-B + math.sqrt(delta))/(2*A)
         x2 = (-B - math.sqrt(delta))/(2*A)
         print("as raizes dessa equação são: ", x1, "e", x2)






