# Forma ideal

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for n in range(len(my_list) - 1, -1, -1):
    if my_list[n] not in new_list:
        new_list.append(my_list[n])

    else:
        continue

swapped = True

while swapped:

    swapped = False

    for i in range(len(new_list) - 1):
        if new_list[i] > new_list[i + 1]:
            swapped = True
            new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
#
# Escribe tu código aquí.
#
print("La lista con elementos únicos:")
print(new_list)
print(my_list, "Lista vieja")


# FORMA NO IDEAL

my_list = [1, 111, 20, 2, 4, 4, 1, 4, 2, 6, 2, 9]

lista2 = my_list[:]
conjunto = set(lista2)
# print conjunto (conjunto elimina los duplicados)
print(lista2, "Es una copia de la lista 1")

swapped = True

while swapped:

    swapped = False

    for i in range(len(lista2) - 1):
        if lista2[i] > lista2[i + 1]:
            swapped = True
            lista2[i], lista2[i + 1] = lista2[i + 1], lista2[i]
print(lista2, "Esta es la lista ordenada: ")

for i in range(len(lista2) - 1):
    if (lista2[0]) != [0]:
        continue
        # if i in range (len (lista2[0]) == [0] :
        break


# Escribe tu código aquí.
#
print("La lista con elementos únicos:")
print(conjunto)
