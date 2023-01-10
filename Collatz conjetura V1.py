def collatz(num):
    c0 = [num]

    while int(num > 1):

        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        c0.append(num)
    return c0


secuencia = collatz(16)

contador = 0

for i in secuencia:
    contador += 1
    contador - 1
for i in secuencia:
    print(i, " ")

print("Pasos = ", contador)
