# determinar la calidad de dìas de un mes ingresado por el usuario


def cantidad_dias(mes):
    if mes.lower() in ("enero", "marzo" "julio" "agosto" "octubre" "diciembre"):
        return "31"
    elif mes.lower() == "febrero":
        return "28/29"
    else:
        return "30"


name_month = input("Ingrese el nombre del mes: ")

print(cantidad_dias(name_month))

# cantidad de dias de un mes de un año especifico

from calendar import monthrange


def cantdiasmes(month, year):
    return monthrange(year, month)[1]


print(cantdiasmes(2, 2020))
