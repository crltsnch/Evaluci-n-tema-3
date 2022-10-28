from re import X
from tkinter import Y
import sympy
p1=input("Dime un polinomio: ")
p2=input("Dime otro polinomio: ")
print("n")
sympy.init_printing()
x=sympy.simbols('x')
y=sympy.simbols('y')
poli1=sympy.Poly(p1)
poli2=sympy.Poly(p2)

def res(p1, p2):
    return p1-p2
def div(p1, p2):
    return p1/p2


