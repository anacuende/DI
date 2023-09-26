import random

puntosJugador = 0
puntosMaquina = 0
opciones = ["piedra", "papel", "tijera"]

for i in range(5):
	print("Elija su jugada:")
	print("1- Piedra")
	print("2- Papel")
	print("3- Tijera")
	jugador = int(input("Introduzca su opcion (1/2/3): "))

	maquina = random.choice(opciones)
	print("Jugada de la maquina: ", maquina)
	
	if jugador == 1 and maquina == "papel":
		print("Has perdidio, papel gana a piedra")
		puntosMaquina += 1
	elif jugador == 1 and maquina == "tijera":
		print("Has ganado, piedra gana a tijera")
		puntosJugador += 1
	elif jugador == 2 and maquina == "tijera":
		print("Has perdido, tijera gana a papel")
		puntosMaquina += 1
	elif jugador == 2 and maquina == "piedra":
		print("Has ganado, papel gana a piedra")
		puntosJugador += 1
	elif jugador == 3 and maquina == "piedra":
		print("Has perdido, piedra gana a tijera")
		puntosMaquina += 1
	elif jugador == 3 and maquina == "papel":
		print("Has ganado, tijera gana a papel")
		puntosJugador += 1
	else:
		print("Habéis empatado")
	
if puntosJugador > puntosMaquina:
	print("Ganaste")
elif puntosJugador < puntosMaquina:
	print("Perdiste")
else:
	print("Empatasteis")
