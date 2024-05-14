import random

def obtener_eleccion_computadora():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def obtener_eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ['piedra', 'papel', 'tijera']:
        eleccion = input("Entrada inválida. Por favor, elige piedra, papel o tijera: ").lower()
    return eleccion

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def jugar():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    rondas = 10
    contador_victorias = 0
    contador_derrotas = 0
    contador_empates = 0

    for ronda in range(1, rondas + 1):
        print(f"\nRonda {ronda}:")
        usuario = obtener_eleccion_usuario()
        computadora = obtener_eleccion_computadora()

        print(f"Tú elegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(usuario, computadora)
        print(resultado)

        if resultado == "¡Ganaste!":
            contador_victorias += 1
        elif resultado == "Perdiste":
            contador_derrotas += 1
        else:
            contador_empates += 1

    print("\nJuego terminado. Resultados:")
    print(f"Victorias: {contador_victorias}")
    print(f"Derrotas: {contador_derrotas}")
    print(f"Empates: {contador_empates}")

if __name__ == "__main__":
    jugar()
