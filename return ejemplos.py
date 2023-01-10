var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))    # salida: 14


def mult(x):
    var = 5
    return x * var


print(mult(7))    # salida: 35

def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))    # salida: 49


def adding(x):
    var = 7
    return x + var


print(adding(4))    # salida: 11
print(var)    # NameError


var = 2
print(var)    # salida: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())    # salida: 5
print(var)    # salida: 5
