def sumardosnums(num1, num2):
    return num1 + num2


def validar_input(valor, vmin, vmax):
    try:
        num_val = int(valor)
        if vmin <= num_val <= vmax:
            return num_val
        else:
            raise TypeError
    except (TypeError, ValueError):
        return None
    try:
        nums_comparar = int(valor)
        if vmin <= nums_comparar <= vmax:
            return nums_comparar
        else:
            raise TypeError
    except (TypeError, ValueError):
        return None


class pedir_input:
    num_val = []
    nums_comparar = []

    def __init__(self):
        self.num_val.append(input("Ingrese la cantidad de valores a verificar: "))
        self.nums_comparar.append(input("Ingrese el numero a sumar: "))


numero1 = pedir_input()
numero1(validar_input(0, 1, 5))
numero1(validar_input(0, -1000, 1000))


"""
if __name__ == "__main__":
    num_veces = 
    param_list = []
    for i in (num_veces):
        param_list.append(i)                

   
        
        if param is None:
            print("Valor incorrecto, intente de nuevo.")
    return param


def get_num_veces():
    param = None
    while param is None:
        param1_str = input("Ingrese la cantidad de valores a verificar: ")
        param = validar_input(param1_str, 1, 5)
        if param is None:
            print("Valor incorrecto, intente de nuevo.")
    return param



if __name__ == "__main__":
    num_veces = get_num_veces()
    param_list = []
    for i in range(num_veces):
        param_list.append(get_input())

"""
