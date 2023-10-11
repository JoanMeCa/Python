Num = 1
Numers = 0
Contador = 0
Max = -9999999999999999999999999999
Min = 99999999999999999999999999999
while Num != 0:
    Num = int(input("Escriba un número: "))
    if Num > Max:
        Max = Num
    if Num < Min:
        Min = Num
    Contador = Contador + 1
    Numers = Numers + Num
Media = Numers / Contador
print("Con los números dados, la media es", Media, "y el máximo y el mínimo de los números dados son, respectivamente:", Max, Min)