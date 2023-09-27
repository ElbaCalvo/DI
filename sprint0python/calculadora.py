from operaciones import suma, resta, multiplicacion, division

print("\nCALCULADORA:")
while True:
    
    i = int(input("\n- Primer número: "))
    j = int(input("\n- Segundo número: "))

    print("\n1.- Suma.")
    print("2.- Resta.")
    print("3.- Multiplicación.")
    print("4.- División.")
    op = int(input("\n- Que operación quieres hacer? "))

    while (op != 1) and (op != 2) and (op != 3) and (op != 4):
        print ("\n[!] La opción no es válida.")
        op = int(input("\n- Que operación quieres hacer? "))

    if op==1:
        print("\nLa suma de {} y {}".format(i,j), "es", suma(i,j), "\n")
    elif op==2:
        print("\nLa resta de {} y {}".format(i,j), "es", resta(i,j), "\n")
    elif op==3:
        print("\nLa multiplicación de {} y {}".format(i,j), "es", multiplicacion(i,j), "\n")
    elif op==4:
        print("\nLa división de {} y {}".format(i,j), "es", division(i,j), "\n")
    
    rep = input("\n- Desea hacer otra operación (s/n)? ").lower()
    if rep != 's' and rep !='n':
        print("\n[!] Tienes que insertar s o n.")
        rep = input("\n- Desea hacer otra operación (s/n)? ").lower()
    if rep == 's':
        print("\n---------------------------------------------\n")
        print("NUEVA OPERACIÓN")
        True
    else:
        print("\n-------------- FIN DEL PROGRAMA --------------\n")
        break


