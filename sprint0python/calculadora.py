from operaciones import suma, resta, multiplicacion, division

respuesta = "s"
print("Introduzca dos números")
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))

while respuesta == "s":
        print("Operaciones")
        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicacion")
        print("4- Division")
        op = int(input("Seleccione operacion (1/2/3/4): "))

        if op == 1:
                resultado = suma(a, b)
                print({resultado})
        elif op == 2:
                resultado = resta(a, b)
                print({resultado})
        elif op == 3:
                resultado = multiplicacion(a, b)
                print({resultado})
        else:
                resultado = division(a, b)
                print({resultado})

        respuesta = input("¿Desea realizar otra operación (s/n)? ")
        if respuesta != "s":
                break
