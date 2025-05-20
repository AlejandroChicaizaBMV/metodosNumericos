import math

def evaluar(x):
    #Función con la que se aplicará el método de la secante
    return  redondear(x**4 -x -1)

def redondear(numero):
    return round(numero, 8)

def algoritmoClase(p0, p1, tolerancia, numeroIteraciones):
    #paso 1
    i = 2
    q0 = evaluar(p0)
    q1 = evaluar(p1)
    #paso 2
    while i <= numeroIteraciones:
        #paso 3
        puntoMedio = redondear(p1 - (q1 * (p1-p0)/(q1-q0)))
        
        print(f"{p0} & {p1} & {puntoMedio} & {q0} & {q1} &",evaluar(puntoMedio),"&",redondear(abs(puntoMedio - p1)),"\\\\")

        #paso 4
        if(abs(puntoMedio - p1)) < tolerancia:
            print(f"p = {puntoMedio}")
            break
        #paso 5
        i = i +1
        #paso 6
        p0 = p1
        q0 = q1
        p1 = puntoMedio
        q1 = evaluar(puntoMedio)
    #paso 7 
    print("---Fin del algoritmo---")



p0 = float(input("primera raiz (p0):"))
p1 = float(input(f"p0 = {p0}, p1: "))
numeroIteraciones = int(input("Numero de iteraciones: "))
print(f"(p0,p1) = [{p0}, {p1}]")

tolerancia = 10**(-5)

algoritmoClase(p0, p1, tolerancia, numeroIteraciones)
