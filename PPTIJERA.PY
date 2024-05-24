#JUEGO DE PIEDRA PAPEL O TIJERA "BRYAN CEVALLOS"

import random      #Importamos una libreria para elegir elementos al azar

def maquina():           #Definimos las opciones de que  tendra la computadora
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)    #random.choice  permite seleccionar las opciones definidas aleatoriamente

def elecciones_jugador():       
    eleccion = input("Seleccione entre piedra, papel o tijera: ").lower() #utilizamos lower para que todas las entradas esten en minusculas
    while eleccion not in ['piedra', 'papel', 'tijera']: # Se utiliza not in para comprovar si la entrada es true o false
        eleccion = input("Eleccion incorrecta las opciones disponibles son: piedra, papel o tijera: ").lower()
    return eleccion

def saber_ganador(jugador, pc): # Se define las condiciones y las variables para definir un ganador
    if jugador == pc:  # Comparamos si son iguales y se devuelve un mensaje en caso de ser true caso contrario elif
        return "Esta ronda es un Empate"
    elif (jugador == 'piedra' and pc == 'tijera') or \
         (jugador == 'papel' and pc == 'piedra') or \
         (jugador == 'tijera' and pc == 'papel'): #En esta parte simplemte se define las opciones cuando el jugador seria el ganaador
        return "¡Ganaste esta ronda!"
    else:
        return "Perdiste esta ronda" #Si ninguna de las dos condiciones anteriores es verdadera devulve este mensaje

def jugar(): # Se define la funcion que llamara a las anteriores para que el juego se ejecute
    print("--------JUEGA PIEDRA PAPEL O TIJERA---------")
    rondas = 10
    contador_victorias = 0
    contador_derrotas = 0
    contador_empates = 0

    for ronda in range(1, rondas + 1):  #Utlizamos range para indicarle a FOR que empieza en 1 hata el valor de rondas=10 y que se incremente de un numero a la vez
        print(f"\nRonda {ronda}:")      
        jugador = elecciones_jugador() # La variable jugador toma el valor de la funcion elecciones_jugador
        pc = maquina()                #la variable pc toma el valor de la funcion maquina

        print(f"Tú elegiste: {jugador}")  # Mostramos las elecciones del jugador y maquina
        print(f"La pc eligió: {pc}")

        resultado = saber_ganador(jugador, pc) # la variable  resultado toma el valor de la funciom saber_ganador
        print(resultado)

        if resultado == "¡Ganaste esta ronda!":   # en esta parte hacemos una comparacion del rsultado 
            contador_victorias += 1               #con lo descrito en la funcion saber_ganador 
        elif resultado == "Perdiste esta ronda":  #para ir contablizando las partidas ganadas, perdidas y empates
            contador_derrotas += 1
        else:
            contador_empates += 1

    print("\nEl juego termino estos son los resultados finales:")# Al final simplemente se imprime los resultados
    print(f"Victorias: {contador_victorias}")                    # que contienen las variables
    print(f"Derrotas: {contador_derrotas}")
    print(f"Empates: {contador_empates}")

if __name__ == "__main__": # Aqui se le indica a python que el programa se ejecutara direcramente sin llamar a alguna funcion de otro archivo
    jugar()
