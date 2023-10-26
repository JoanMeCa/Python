Num = 0
Numers = 0
Contador = 0
Num = int(input("Escriba un número: "))
while Num != -1:
    if Num < -1:
        print("Valor no válido")
        Num = int(input("Escriba un número: "))
    else: 
        if Num != -1:
            Contador = Contador + 1
            Numers = Num + Numers
            Num = int(input("Escriba un número: "))
Resultado = Numers / Contador
print(Resultado)