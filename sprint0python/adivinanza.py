import random

puntos = 0

adivinanzas = [
	{
		"adivinanza": "Tengo agujas pero no sé coser, tengo números pero no sé leer, las horas te doy, ¿Sabes quién soy?",
		"opciones": {
			"a": "Mesa",
			"b": "Reloj",
			"c": "Libro"
		},
		"respuesta_correcta": "b"
	},
	{
		"adivinanza": "Blanco por dentro, verde por fuera, si quieres saberlo, espera. ¿Qué es?",
		"opciones": {
			"a": "Pera",
			"b": "Tomate",
			"c": "Uva"
		},
		"respuesta_correcta": "a"
	},
	{
		"adivinanza": "Tiene llaves pero no abre puertas, tiene espacio pero no tiene habitantes. ¿Qué es?",
		"opciones": {
			"a": "Televisión",
			"b": "Silla",
			"c": "Teclado"
		},
		"respuesta_correcta": "c"
	}
]

selec_adivinanza = random.sample(adivinanzas, 2)

for adivinanza in selec_adivinanza:
	print(adivinanza["adivinanza"])
	for opcion, respuesta in adivinanza["opciones"].items():
		print(f"{opcion}) {respuesta}")
	respuesta = input("Teclee respuesta (a/b/c): ")
	if respuesta == adivinanza["respuesta_correcta"]:
		print("Correcto")
		puntos += 10
	else:
		print(f"Incorrecto, la respuesta es {adivinanza['respuesta_correcta']}")
		puntos -= 5
print("Puntuacion: ", puntos)
