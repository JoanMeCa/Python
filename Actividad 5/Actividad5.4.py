Intentos = 3
Pass = "Awooga"
while Pass !="Eureka" and Intentos > 0:
    Pass = input("Introduzca la contraseña: ")
    if Pass == "Eureka": print("Contraseña Correcta!")
    else: 
        print("ERROR CONTRASEÑA INCORRECTA")
        Intentos = Intentos - 1
        if Intentos <= 0: print("Has gastado todos los intentos, cerrando sistema")
        else: print("Te quedan", Intentos, "intentos.")
    