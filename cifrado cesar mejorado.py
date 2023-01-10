from string import ascii_lowercase, ascii_uppercase

cifrado = []

text = input("Ingresa tu mensaje a encriptar: ")

rango = 0

while rango == 0:
    try:
        rango = int(input("Ingresa un rango numerico del 1 al 25 para encriptar: "))
        if rango not in range(1, 26):
            raise ValueError
    except ValueError:
        rango = 0
    # Mantener el bucle, de lo contrario se sale al segundo intento y genera error.
    if rango == 0:
        print("El valor ingresado no es valido, ingresa un rango numerico del 1 al 25")

for char in text:
    if char in ascii_lowercase:
        indice = ascii_lowercase.index(char)
        nuevoindice = (indice + rango) % len(ascii_lowercase)
        cifrado.append(ascii_lowercase[nuevoindice])

    elif char in ascii_uppercase:
        indice = ascii_uppercase.index(char)
        nuevoindice = (indice + rango) % len(ascii_uppercase)
        cifrado.append(ascii_uppercase[nuevoindice])
    else:
        cifrado.append(char)


print("".join(cifrado))
