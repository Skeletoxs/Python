numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def Primos(maximo):
    for numero in range(maximo):
        if (numero is numeros_primos):
            yield numero
        if (numero > 100):
            break

maximo = 50
for numero in Primos(maximo):
    print(numero)