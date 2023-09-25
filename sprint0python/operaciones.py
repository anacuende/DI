print("Introduce dos valores")
a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))

def suma(a, b):
	resultadoSuma = a + b
	return resultadoSuma

def resta(a, b):
	resultadoResta = a - b
	return resultadoResta

def multiplicacion(a, b):
	resultadoMultiplicacion = a * b
	return resultadoMultiplicacion

def division(a, b):
	if b == 0:
		resultadoDivision = "Infinito"
		return resultadoDivision
	else:
		resultadoDivision = a / b
		return resultadoDivision

resultadoSuma = suma(a, b)
print({resultadoSuma})
resultadoResta = resta(a, b)
print({resultadoResta})
resultadoMultiplicacion = multiplicacion(a, b)
print({resultadoMultiplicacion})
resultadoDivision = division(a, b)
print({resultadoDivision})
