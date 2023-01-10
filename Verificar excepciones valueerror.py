def readint(prompt, min, max):
    try:
        a = int(input("Ingrese un numero entero: "))
        if a > max or a < min:
            print("Error: el valor no está dentro del rango permitido", (min, max))
            a = int(input("Ingrese un numero entero: "))

    except ValueError:
        print("Error: entrada incorrecta")
        a = int(input("Ingrese un numero entero: "))

    return a


v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
