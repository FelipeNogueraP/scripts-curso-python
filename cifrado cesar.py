# Cifrado César
text = input("Ingresa tu mensaje: ")
cifrado = ""
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord("Z"):
        code = ord("A")
    cifrado += chr(code)

print(cifrado)
