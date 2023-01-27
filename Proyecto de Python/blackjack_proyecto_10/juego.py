import random
import replit


#Fuciones para el juego
def generar_carta():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta = random.choice(cartas)
    return carta

def sumar_cartas(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def mostrar_ganador(marcador_usuario, marcador_ordenador):
    if marcador_usuario == marcador_ordenador:
        texto = "Empate"
    elif marcador_ordenador == 0:
        texto = "Has perdido... la maquina tiene 21-Blackjack, eres inferior a la maquina"
    elif marcador_usuario == 0:
        texto = "Has ganado... demostraste tu superioridad tienes 21-Blackjack"
    elif marcador_usuario > 21:
        texto = "Has perdido... la suma de tus cartas es mayor de 21, tubiste que quedarte"
    elif marcador_ordenador > 21:
        texto = "Has ganado... la maquina tiene mas de 21, que avaricia"
    elif marcador_usuario > marcador_ordenador:
        texto = "Has ganado!!!!! al fin..."
    else:
        texto = "Has perdido... no me sorprende"
    return texto

def jugar():
    print("Estamos jugando...")

    cartas_usuario = []
    cartas_ordenador = []
    finalizado = False

    for valor in range(2):
        cartas = generar_carta()
        cartas_usuario.append(cartas)

        cartas2 = generar_carta()
        cartas_ordenador.append(cartas2)

    while not finalizado:
        marcador_usuario = sumar_cartas(cartas_usuario)
        marcador_ordenador = sumar_cartas(cartas_ordenador)
        
        print(f"cartas del usuario =  {cartas_usuario}, marcador del usuario {marcador_usuario}")
        print(f"cartas de la maquina {cartas_ordenador[0]}")

        if marcador_usuario == 0 or marcador_ordenador == 0 or marcador_usuario > 21:
            finalizado = True
        else:
            mas_cartas = input("¿Quieres mas cartas?. Escribe 'si' o 'no'")
            if mas_cartas == 'si':
                cartas = generar_carta()
                cartas_usuario.append(cartas)
            else:
                finalizado = True

    while marcador_ordenador != 0 and marcador_ordenador < 17:
        cartas2 = generar_carta()
        cartas_ordenador.append(cartas2)
        marcador_ordenador = sumar_cartas(cartas_ordenador)

    print(f"cartas del usuario =  {cartas_usuario}, marcador del usuario {marcador_usuario}")
    print(f"cartas de la maquina {cartas_ordenador}, marcador de la maquina {marcador_ordenador}")

    texto = mostrar_ganador(marcador_usuario, marcador_ordenador)
    print(texto)


#Principios del programa 
while input("¿Quieres jugar BlackJack?. Escribe 'si' o 'no'") == 'si':
    replit.clear()
    jugar()

