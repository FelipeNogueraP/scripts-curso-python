income = float(input("Introduce el ingreso anual:"))

if income <= 85528:

    tax = income * 0.18 - 556.2

elif income >= 85529:

    diferencia = income - 85528

    diferenciaPorc = diferencia * 0.32

    tax = diferenciaPorc + 14839.2


tax = round(tax, 0)

if tax <= -1:
    print("El impuesto es", 0.0, "Pesos")

else:

    print("El impuesto es:", tax, "pesos")


# ingreso = float(input("Ingresa el ingreso anual:"))

if ingreso < 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - 85528) * 0.32 + 14839.02

if impuesto < 0.0:
    impuesto = 0.0

impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")
