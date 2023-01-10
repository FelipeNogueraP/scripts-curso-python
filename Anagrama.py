def anagrama(primero, segundo):
    primero = primero.replace(" ", "")
    primero = primero.upper()
    segundo = segundo.replace(" ", "")
    segundo = segundo.upper()

    validacion = sorted(primero) == sorted(segundo)
    if validacion == False:
        return "No son Anagramas"
    else:
        return "Si son Anagramas"


primero = input("Ingrese la Primera palabra: ")
segundo = input("Ingrese la Segunda palabra: ")

print(anagrama(primero, segundo))
