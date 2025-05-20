import math
def redondear(numero):
    return round(numero, 8)
def evaluar(x):
    return  redondear(x**4 -x -1)

def algoritmoClase(p0, p1, tolerancia, numeroIteraciones):
    #Paso 1
    i = 2
    q0 = evaluar(p0)
    q1 = evaluar(p1)
    
    #Paso 2 
    while i <= numeroIteraciones:
        #Paso 3 
        p = redondear(p1 - q1 *((p1 - p0)/(q1-q0)))

        print(f"{p0} & {p1} & {p} & {q0} & {q1} & ", evaluar(p)," & ", redondear(abs(p - p1)),"\\\\")
        #Paso 4
        if abs(p - p1) < tolerancia:
            print("p = ", p)
            break

        #Paso 5
        i = i + 1
        q = evaluar(p)
        
        #Paso 6
        if q*q1 < 0:
            p0 = p1
            q0 = q1
        
        #Paso 7
        p1 = p 
        q1 = q
        
        #Paso 8

    print("-- FIN del algoritmo ---")

p0 = float(input("p0 = "))
p1 = float(input("p1 = "))
tolerancia = 10**(-6)
numeroIteraciones = int(input("Número de iteraciones: "))

algoritmoClase(p0, p1, tolerancia, numeroIteraciones)