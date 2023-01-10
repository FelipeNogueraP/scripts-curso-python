def hello(name):  # definiendo una función
    print("Hola,", name)  # cuerpo de la función


name = input("Ingresa tu nombre: ")

hello(name)  # invocación de la función


# forma ideal de definir funciones


def message():
    print("Ingresa un valor: ")


message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
