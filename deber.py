import math


def truncar(numero, cifras):
    if numero == 0: 
        return 0
    else: 
        orden = int (math.floor(math.log10(abs(numero))))

        factor = 10**(cifras -1 -orden)
        numero_truncado = math.trunc(numero * factor) / factor
        return numero_truncado 

def redondear(numero, cifras):
    if numero == 0:
        return 0
    else:
        orden = int(math.floor(math.log10(abs(numero))))
        factor = 10**(cifras -1 -orden)
        numero_redondeado = round(numero * factor) / factor
        return numero_redondeado
    
def errorReal(valorReal, valorAproximado):
    return valorReal - valorAproximado
    
def errorAbsoluto(valorReal, valorAproximado):
    return abs(valorReal - valorAproximado)
    
def errorRelativo(valorReal, valorAproximado):
    return abs((valorReal - valorAproximado)/valorReal)

def errorPorcentual(valorReal, valorAproximado):
    return abs((valorReal - valorAproximado)/valorReal) * 100

pi = (1/3)
print("Constante pi sin truncamiento a 4 cifras significativas:", pi)

pi_truncado = truncar(pi, 4)
pi_redondeado = redondear(pi, 4)

print("Número truncado a 4 cifras significativas:", pi_truncado)
print("Número redondeado a 4 cifras significativas:", pi_redondeado)

print("(valor truncado) Error Real:", errorReal(pi, pi_truncado), "\n"
      "Error Absoluto:", errorAbsoluto(pi, pi_truncado), "\n"
      "Error Relativo:", errorRelativo(pi, pi_truncado), "\n"
      "Error Porcentual:", errorPorcentual(pi, pi_truncado))


print("(valor redondeado) Error Real:", errorReal(pi, pi_redondeado), "\n"
      "Error Absoluto:", errorAbsoluto(pi, pi_redondeado), "\n"
      "Error Relativo:", errorRelativo(pi, pi_redondeado), "\n"
      "Error Porcentual:", errorPorcentual(pi, pi_redondeado))