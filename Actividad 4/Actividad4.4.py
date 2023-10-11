A = int(input("Establezca el valor de A: "))
B = int(input("Establezca el valor de B: "))
C = int(input("Establezca el valor de C: "))
if A == B and A == C: Respuesta = print("Los tres valores son iguales")
else:
    if A > B: 
        if A > C: Respuesta = print(A, "es superior a", B, "y", C)
        else: 
            if C > A: Respuesta = print(A, "es superior a", B, "pero inferior a", C)
            else: Respuesta = print(A, "es superior a", B, "pero igual a", C)
    else: 
        if B > C: Respuesta = print(B, "es superior a", A, "y", C)
        else: 
            if C > B: Respuesta = print(B, "es superior a", A, "pero inferior a", C)
            else: Respuesta = print(B, "es superior a", A, "pero igual a", C)