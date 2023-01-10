# Invertir el orden de la lista con bucle For

miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range(longitud // 2):
    miLista[i], miLista[longitud - i - 1] = miLista[longitud - i - 1], miLista[i]

print(miLista)
