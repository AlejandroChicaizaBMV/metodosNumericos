import math

def evaluar(x):
    #Función con la que se aplicará el método de bisección
    return redondear(math.sin(math.pi*x))

def redondear(numero):
    return round(numero, 6)

def algoritmoClase(limiteInferior, limiteSuperior, tolerancia, numeroIteraciones):
    #Paso 1
    i = 1
    FA = evaluar(limiteInferior)
    
    #Paso 2
    while i <= numeroIteraciones:
        #Paso 3
        puntoMedio = redondear(limiteInferior + (limiteSuperior - limiteInferior)/2)
        FP = evaluar(puntoMedio)
        
        print(f"{limiteInferior} & {limiteSuperior} & {puntoMedio} & {FA} &", evaluar(limiteSuperior),f"& {FP} &",redondear((limiteSuperior-limiteInferior)/2),"\\\\")
        #Paso 4
        if(FP == 0 or (limiteSuperior - limiteInferior)/2 < tolerancia):
            print(f"p = {FP}")
            break

        #Paso 5
        i = i + 1
        #Paso 6
        if(FA*FP > 0):
            limiteInferior = puntoMedio
            FA = FP
        else:
            limiteSuperior = puntoMedio
    #Paso 7
    print(f"El método fracasó después de {numeroIteraciones} intentos. :c")    

limiteInferior = float(input("Limite infeior (desde):"))
limiteSuperior = float(input(f"Interalo desde {limiteInferior}, (Hasta): "))
numeroIteraciones = int(input("Numero de iteraciones: "))
print(f"Intervalo seleccionado:[{limiteInferior}, {limiteSuperior}]")

tolerancia = 10**(-4)

algoritmoClase(limiteInferior, limiteSuperior, tolerancia, numeroIteraciones)
