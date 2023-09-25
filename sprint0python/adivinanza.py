puntos = 0
print("Tengo agujas pero no sé coser, tengo números pero no sé leer, las horas te doy, ¿Sabes quién soy?")
print("a) Mesa")
print("b) Reloj")
print("c) Libro")
respuesta = input("Teclee respuesta (a/b/c): ")
if respuesta != "b":
	print("Incorrecto, la respuesta correcta es B")
	puntos = puntos - 5
else:
	print ("Correcto")
	puntos = puntos + 10
print("Blanco por dentro, verde por fuera, si quieres saberlo, espera. ¿Qué es?")
print("a) Pera")
print("b) Tomate")
print("c) Uva")
respuesta = input("Teclee respuesta (a/b/c): ")
if respuesta != "a":
	print("Incorrecto, la respuesta correcta es A")
	puntos = puntos - 5
else:
	print("Correcto")
	puntos = puntos + 10
print("Tiene llaves pero no abre puertas, tiene espacio pero no tiene habitantes. ¿Qué es?")
print("a) Televisión")
print("b) Silla")
print("c) Teclado")
respuesta = input("Teclee respuesta (a/b/c): ")
if respuesta != "c":
	print("Incorrecto, la respuesta es C")
	puntos = puntos - 5
else:
	print("Correcto")
	puntos = puntos + 10
print("Tu puntuación final es: ", puntos)
