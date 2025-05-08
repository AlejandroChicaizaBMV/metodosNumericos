import math
import sympy as sp

def evaluar_funciones(x_valor):
    # Sustituir el valor en la función original y derivada
    valor_f = f.subs(x, x_valor).evalf()
    valor_f_derivada = f_derivada.subs(x, x_valor).evalf()
    return valor_f, valor_f_derivada

def redondear(numero):
    return round(numero, 13)

def algoritmoClase(p0, tolerancia, numeroIteraciones):
    #paso 1
    i = 1
    
    #paso 2
    while i<= numeroIteraciones:
        #paso 3 
        f_p0, f_derivada_p0 = evaluar_funciones(p0)
        f_p0 = redondear(f_p0)
        f_derivada_p0 = redondear(f_derivada_p0)
        p = redondear(p0 - f_p0/f_derivada_p0)
        
        print(f"{p0} & {p} & {f_p0} & {f_derivada_p0} & ", redondear(abs(p - p0)),"\\\\")
        #paso 4 
        if abs(p - p0) < tolerancia:
            print(f"p = {p}")
            break

        #paso 5
        i = i + 1
        #paso 6 
        p0 = p 
    print("--- Fin del algoritmo ---")



p0 = float(input("primera raiz (p0):"))
numeroIteraciones = int(input("Numero de iteraciones: "))
print(f"p0 = [{p0}]")

tolerancia = 10**(-16)

x = sp.Symbol('x')

f = sp.cos(x) - x

f_derivada = sp.diff(f, x)

algoritmoClase(p0, tolerancia, numeroIteraciones)