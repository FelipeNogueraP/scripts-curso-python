# Puedes pasar argumentos a una función utilizando las siguientes técnicas:

# Paso de argumentos posicionales en la cual el orden de los parámetros es relevante (Ejemplo 1).
# Paso de argumentos con palabras clave en la cual el orden de los argumentos es irrelevante (Ejemplo 2).
# Una mezcla de argumentos posicionales y con palabras clave (Ejemplo 3).
# Ejemplo 1
def subtra(a, b):
    print(a - b)


subtra(5, 2)  # salida: 3
subtra(2, 5)  # salida: -3


# Ejemplo 2
def subtra(a, b):
    print(a - b)


subtra(a=5, b=2)  # salida: 3
subtra(b=2, a=5)  # salida: 3

# Ejemplo 3
def subtra(a, b):
    print(a - b)


subtra(5, b=2)  # salida: 3
subtra(5, 2)  # salida: 3
