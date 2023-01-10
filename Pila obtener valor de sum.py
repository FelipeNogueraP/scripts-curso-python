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

    def getSuma(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val


objetoPila = SumarPila()

for i in range(5):
    objetoPila.push(i)
print(objetoPila.getSuma())

for i in range(5):
    print(objetoPila.pop())
