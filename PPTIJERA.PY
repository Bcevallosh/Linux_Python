import random

def maquina():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def elecciones_jugador():
    eleccion = input("Seleccione entre piedra, papel o tijera: ").lower()
    while eleccion not in ['piedra', 'papel', 'tijera']:
        eleccion = input("Eleccion incorrecta las opciones disponibles son: piedra, papel o tijera: ").lower()
    return eleccion

def saber_ganador(jugador, pc):
    if jugador == pc:
        return "Esta ronda es un Empate"
    elif (jugador == 'piedra' and pc == 'tijera') or \
         (jugador == 'papel' and pc == 'piedra') or \
         (jugador == 'tijera' and pc == 'papel'):
        return "¡Ganaste esta ronda!"
    else:
        return "Perdiste esta ronda"

def jugar():
    print("--------JUEGA PIEDRA PAPEL O TIJERA---------")
    rondas = 10
    contador_victorias = 0
    contador_derrotas = 0
    contador_empates = 0

    for ronda in range(1, rondas + 1):
        print(f"\nRonda {ronda}:")
        jugador = elecciones_jugador()
        pc = maquina()

        print(f"Tú elegiste: {jugador}")
        print(f"La pc eligió: {pc}")

        resultado = saber_ganador(jugador, pc)
        print(resultado)

        if resultado == "¡Ganaste esta ronda!":
            contador_victorias += 1
        elif resultado == "Perdiste esta ronda":
            contador_derrotas += 1
        else:
            contador_empates += 1

    print("\nEl juego termino estos son los resultados finales:")
    print(f"Victorias: {contador_victorias}")
    print(f"Derrotas: {contador_derrotas}")
    print(f"Empates: {contador_empates}")

if __name__ == "__main__":
    jugar()
