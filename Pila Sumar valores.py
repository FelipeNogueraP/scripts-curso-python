class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0
