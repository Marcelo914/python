import math
from re import A, X
from this import d
from tkinter import Y

A =int(input("valor de A: "))
B = int(input("valor de B: "))
C = int(input("valor de C: "))

delta = B**2 -(4 * A * C)
if delta== 0:
    X = (-B + 0) //(A*2)
    print("A raiz dessa equação é: ", int(X))
if delta < 0:
    print ("Essa equação não possui raizes reais.")
if delta > 0:
    x1 = -B + math.sqrt(delta)/2*A
    x2 = -B - math.sqrt(delta)/2*A
    print("As raizes da equação são:", int(x1), "e" ,  int(x2) )
