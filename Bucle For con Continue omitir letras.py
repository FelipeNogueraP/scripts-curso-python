user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

for letter in user_word:
    if letter in ("A,E,I,O,U"):
        continue
    print(letter)
