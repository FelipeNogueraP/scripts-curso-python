"""userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for i in userWord:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue
    else:
        print(i)
"""

palabraSinVocal = ""

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabraSinVocal = palabraSinVocal + letra
        continue

print(palabraSinVocal)
