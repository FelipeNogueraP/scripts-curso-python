class SuperA:
    varA = 10

    def funA(self):
        return 11


class SuperB:
    varB = 20

    def funB(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.varA, obj.funA())
print(obj.varB, obj.funB())
