adivinanza1 = {
    'ad1':'¿Qué se encuentra una vez en un minuto, dos veces en un momento pero ninguno en cien años?', 'a':'El silencio.', 'b':'La letra m.', 'c':'El día de mañana.'
}

adivinanza2 = {
    'ad2':'Redondo, redondo, barril sin fondo. ¿Qué es?', 'a':'Un anillo.', 'b':'Una campana.', 'c':'La sombra.'
}

adivinanza3 = {
    'ad3':'Existo cuando me guardan, muero cuando me sacan.', 'a':'La letra h.', 'b':'El abanico.', 'c':'Un secreto.'
}

for x in adivinanza1.items():
    print(adivinanza1[x])
    
print(adivinanza2)
print(adivinanza3)

resp = input("\n- Que opción es la correcta? ")
respMin = resp.lower()

while (respMin != "a") & (respMin != "b") & (respMin != "c"):
    print ("\n[!] La respuesta marcada no es válida.")
    resp = input("\n- Que opción es la correcta? ")
    respMin = resp.lower()

if respMin=="b":
    print ("\nHas respondido bien, enorabuena!\n")
else:
    print ("\nHas fallado... Vuelve a intentarlo.\n")



