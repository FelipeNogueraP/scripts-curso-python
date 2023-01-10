class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

if hasattr(objetoEjemplo, "b"):
    print(objetoEjemplo.b)
