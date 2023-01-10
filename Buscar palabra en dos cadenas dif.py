palabra = input("Ingresa la palabra que deseas encontrar: ").upper()
cadena = input("Ingresa la cadena en donde deseas buscar: ").upper()

encontrada = True
inicio = 0

for ch in palabra:
    pos = cadena.find(ch, inicio)
    if pos < 0:
        encontrada = False
        break
    inicio = pos + 1
if encontrada:
    print("Si")
else:
    print("No")
