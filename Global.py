def return_var():
    global var
    var = 5
    return var


print(return_var())  # salida: 5
print(var)  # salida: 5
