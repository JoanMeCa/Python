import math
A = int(input("Establezca el valor de A: "))
Resultado = "Error, valor no válido"
if A <= 0: print(Resultado)
else: 
    Raiz = math.sqrt(A)
    Cuadrado = A * A
    print("La raíz cuadrada de", A, "es", Raiz, "y elevado a 2 da", Cuadrado)