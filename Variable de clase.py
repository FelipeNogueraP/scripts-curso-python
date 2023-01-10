class ClaseEjemplo:
    __contador = 0

    def __init__(self, val=1):
        self.__primera = val
        ClaseEjemplo.__contador += 1


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1._ClaseEjemplo__contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2._ClaseEjemplo__contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3._ClaseEjemplo__contador)
