blocks = int(input("Ingresa el número de bloques: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("La altura de la pirámide:", height)

"""lo que hace el codigo es arrancar de 0 de altura, sumarle 1 a las capas,
 a los bloques les resta el numero de capas en las que vamos
 a las capas le suma 1.

va descontando bloques y sumando capas, a la vez que suma en altura."""
