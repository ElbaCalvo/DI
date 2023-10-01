from random import choice

print('\nJUEGO DEL AHORCADO')
b = True
palIncog = ''

while b:
    print('-------------------------------')
    print('\nEscoge la dificultad:\n  1- Fácil (3 a 5 letras)\n  2- Normal (6 a 9 letras)\n  3- Difícil (Más de 9 letras)\n')
    dif=int(input('[?] Opción: '))

    while dif not in [1, 2, 3]:
        print('[!] Valor no válido (1/2/3)')
        dif=int(input('\n[?] Opción: '))
    print('-------------------------------')

    if dif == 1:
        modo ='facil'
    elif dif == 2:
        modo = 'normal'
    elif dif == 3:
        modo = 'dificil'

    pal=''

    with open('palabras.txt', 'r') as j:
        pal = j.read().splitlines()
        pal = [p for p in pal if len(p) >= 3 and len(p) <= 5 and p!='facil'] if modo == 'facil' else [p for p in pal if len(p) >= 6 and len(p) <= 9 and p!='normal'] if modo == 'normal' else [p for p in pal if len(p) > 9 and p!='dificil'] if modo == 'dificil' else None
        if pal:
            pal = choice(pal)
        else:
            print("[!] No se encontraron palabras para el modo seleccionado.")
            b = False
            continue

    letProb=''
    palIncog = '_' * len(pal)

    print(palIncog)
    intentos=0
    
    while intentos<6 and palIncog!=pal:
        aux=''
        let=input('\n[+] Letra escogida: ')

        for i in range(len(pal)):
            if let==pal[i]:
                aux = aux + let
            else:
                aux = aux + palIncog[i]

        if aux == palIncog:
            intentos += 1
            letProb = letProb + let + ' '

        palIncog = aux
        

        print ('\n'+palIncog)
        print ('\n[+] Errores: '+str(intentos))
        print ('[+] Letras falladas: '+ letProb)
        print('\n-------------------------------')

    if intentos >= 6:
        print ('\n[!] Has perdido, la palabra correcta es '+ pal)
    else:
        print ('\n[!] Has ganado!!')

    if input('\n[?] Volver a jugar (s/n)? ') != 's':
        b = False