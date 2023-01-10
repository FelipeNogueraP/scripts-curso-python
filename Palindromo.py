def palindromo(text):
    text = text.replace(" ", "")
    text = text.upper()
    a = 0
    b = len(text) - 1

    for i in range(0, len(text)):
        if text[a] == text[b]:
            a += 1
            b -= 1
        else:
            return "No es Palindromo"

    return "Si es Palindromo"


text = input("Ingrese el texto a verificar: ")

print(palindromo(text))
