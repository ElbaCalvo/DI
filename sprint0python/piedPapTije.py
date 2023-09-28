import random

juego_dic = [
    {
        'nombre' : 'papel',
        'rompe' : 'tijera'
    },

    {
        'nombre' : 'piedra',
        'rompe' : 'papel'
    },

    {
        'nombre' : 'tijera',
        'rompe' : 'piedra'
    }
]

punt1 = 0
punt2 = 0
print('\nJUEGO: PIEDRA PAPEL TIJERA')

for i in range(6):
    print('\n----------------------------')
    jug1 = input('\n[?] Que jugada escoges? ').lower()

    while (jug1 != 'piedra') and (jug1 != 'papel') and (jug1 != 'tijera'):
        print('\n----------------------------')
        print('\n[!] La opción no es válida.')
        print('\n----------------------------')
        jug1 = input('\n[?] Que jugada escoges? ').lower()

    jug2 = random.choice(['piedra', 'papel', 'tijera'])
    print('\n[!] El jugador 2 ha escogido ' + jug2)

    for j in juego_dic:
        if jug1 == j['nombre']:
            break

    for t in juego_dic:
        if jug2 == t['nombre']:
            break

    if j['rompe'] == t['nombre']:
        punt2+=1
        print('\n\n--> El jugador 2 ({}) GANA al jugador 1 ({})'.format(jug2, jug1))
        print('\n--> Jug2 +1pt')
    elif j['nombre'] == t['rompe']:
        punt1+=1
        print('\n\n--> El jugador 1 ({}) GANA al jugador 2 ({})'.format(jug1, jug2))
        print('\n--> Jug1 +1pt')
    else:
        i-=1
        print('\n--> El jugador 1 ({}) EMPATA con el jugador 2 ({})'.format(jug1, jug2))
        print('\n--> No se suman puntos.')

print('\n----------------------------')
print('\nPuntaje final: Jugador 1 (',punt1, 'pts ) / Jugador 2 (',punt2, 'pts )')
print('\nFIN DE PARTIDA\n')

        

