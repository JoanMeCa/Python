A = int(input("Establezca el valor de A: "))
B = int(input("Establezca el valor de B: "))
C = int(input("Establezca el valor de C: "))
if A == B and A == C: Respuesta = print("Los tres valores son iguales")
else:
    if A == B or A == C or B == C:
        if A == B:
            if A > C: Respuesta = print(A, "y", B, "son iguales y superiores a", C)
            else: Respuesta = print(A, "y", B, "son iguales pero inferiores a", C)
        if A == C: 
            if A > B: Respuesta = print(A, "y", C, "son iguales y superiores a", B)
            else: Respuesta = print(A, "y", C, "son iguales pero inferiores a", B)
        if B == C:
            if A > B: Respuesta = print(B, "y", C, "son iguales y superiores a", A)
            else: Respuesta = print(B, "y", C, "son iguales pero inferiores a", A)
    else:
        if A > B:
            if A > C: Respuesta = print(A, "es superior a", B, "y", C)
            else: Respuesta = print(A, "es superior a", B, "pero inferior a", C)
        if B > A:
            if B > C: Respuesta = print(B, "es superior a", A, "y", C)
            else: Respuesta = print(B, "es superior a", A, "pero inferior", C)