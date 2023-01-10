# Compresión de lista
# Forma corta

[expression for element in list if conditional]

# Forma larga

for element in list:
    if conditional:
        expression


# Bidimensional

cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]


#  Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [
    [":(", ":)", ":(", ":)"],
    [":)", ":(", ":)", ":)"],
    [":(", ":)", ":)", ":("],
    [":)", ":)", ":)", ":("],
]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# Cubo - un arreglo tridimensional (3x3x3)

cube = [
    [[":(", "x", "x"], [":)", "x", "x"], [":(", "x", "x"]],
    [[":)", "x", "x"], [":(", "x", "x"], [":)", "x", "x"]],
    [[":(", "x", "x"], [":)", "x", "x"], [":)", "x", "x"]],
]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
