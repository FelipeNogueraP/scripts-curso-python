pila = []


def push(val):
    pila.append(val)


def pop():
    val = pila[-1]
    del pila[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
