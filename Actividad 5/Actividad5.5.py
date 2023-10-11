Numero = int(input("Introduzca un número para calcular su factorial: "))
if Numero < 0: 
    print("Valor no válido, no se puede calcular un valor negativo")
else:
    factorial = 1
    i = 1
    while i <=Numero:
        factorial = factorial * i
        i = i + 1
    print("El factorial de", Numero, "es", factorial)
