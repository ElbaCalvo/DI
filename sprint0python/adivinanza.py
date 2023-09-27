list_dic = [
    {
        'ad':'¿Qué se encuentra una vez en un minuto, dos veces en un momento pero ninguno en cien años?',
        'resp': ['a) El silencio', 'b) La letra m.', 'c) El día de mañana.'],
        'correc':'b'
    },

    {
        'ad':'Redondo, redondo, barril sin fondo. ¿Qué es?',
        'resp': ['a) Un anillo.', 'b) Una campana.', 'c) La sombra.'],
        'correc':'a'
    },

    {
        'ad':'Existo cuando me guardan, muero cuando me sacan.',
        'resp': ['a) La letra h.', 'b) El abanico.', 'c) Un secreto.'],
        'correc':'c'
    }
]

i = 0
punt = 0

for adiv in list_dic:
    
    adivinanza = list_dic[i]['ad']
    respuestas = list_dic[i]['resp']
    correcta = list_dic[i]['correc']
    print ("\nAdivinanza: {} \nRespuestas: {}".format(adivinanza,respuestas))

    resp = input("\n- Que opción es la correcta? ").lower()

    while (resp != 'a') & (resp != 'b') & (resp != 'c'):
        print ("\n[!] La respuesta marcada no es válida.")
        resp = input("\n- Que opción es la correcta? ").lower()

    if resp==list_dic[i]['correc']:
        print ("\nHas respondido bien, enorabuena!\n")
        punt = punt + 10
    else:
        print ("\nHas fallado... Vuelve a intentarlo.\n")
        punt = punt - 5
    
    i=i+1

print ("\n-> Tu puntuación final ha sido: {}\n".format(punt))







