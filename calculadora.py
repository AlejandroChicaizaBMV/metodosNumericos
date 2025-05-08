from fractions import Fraction
import math

def evaluar(x):
    return x - 10**(-4) * x
def evaluar1(x):
    return x + 10**(-4) * x

x = 1.54312312e-19
mantisa, exponente = f"{x:.2e}".split("e")
print(f"{mantisa} \\cdot 10^","{",f"{int(exponente)}","}")
#print((263.3 - 263.2999267578125)/263.3)