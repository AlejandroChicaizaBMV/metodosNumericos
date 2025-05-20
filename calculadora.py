from fractions import Fraction
import math

def evaluar(x):
    return x**(1/3)
def evaluarDerivada(x):
    return 1/3*(x**(-2/3))

print(evaluar(-2))