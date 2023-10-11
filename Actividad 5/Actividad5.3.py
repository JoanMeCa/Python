Dia = int(input("Establezca el día: "))
Mes = int(input("Establezca el mes: "))
if Dia > 31 and Mes > 12: print("Fecha no válida")
else: print("La fecha escrita es", Dia, "/", Mes)