Num = 0
Numers = 0
Contador = 0
while Num != -1:
    Num = int(input("Escriba un número: "))
    Contador = Contador + 1
    Numers = Num + Numers
Resultado = Numers / Contador
print(Resultado)