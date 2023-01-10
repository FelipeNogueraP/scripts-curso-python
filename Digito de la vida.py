digito = list(input("Ingrese su fecha de nacimiento en el formato YYYYMMDD: "))
var = []
total = []

suma = 0
digiV = 0


for i in digito:
    var.append(int(i))
    suma = sum(var)

suma = str(suma)
suma2 = list(suma)

for num in list(suma2):
    total.append(int(num))
    digiV = sum(total)


print(digiV)
