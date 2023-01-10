dict = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
words = ["gato", "leon", "caballo"]

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")
