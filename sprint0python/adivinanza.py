print ("\n¿Qué se encuentra una vez en un minuto, dos veces en un momento pero ninguno en cien años?\n")
print ("a) El silencio.")
print ("b) La letra m.")
print ("c) El día de mañana.")

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



