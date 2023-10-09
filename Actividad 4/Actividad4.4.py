A = int(input("Establezca el valor de A: "))
B = int(input("Establezca el valor de B: "))
C = int(input("Establezca el valor de C: "))
if A > B: 
    if A > C: Respuesta = print(A, "es superior a", B, "y", C)
    else: Respuesta = print(A, "es superior a", B, "pero inferior a", C)
else: 
    if B > C: Respuesta = print(B, "es superior a", A, "y", C)
    else: Respuesta = print(B, "es superior a", A, "pero inferior a", C)