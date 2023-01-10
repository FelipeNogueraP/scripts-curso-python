def introduction(first_name, last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)


introduction("Jorge", "Pérez")

# otra uinvocaciòn
introduction("Enrique")

introduction(first_name="Guillermo")


def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)


introduction()


introduction(last_name="Rodríguez")
