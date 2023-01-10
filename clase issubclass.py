class Vehiculo:
    pass


class VehiculoTerrestre(Vehiculo):
    pass


class VehiculoOruga(VehiculoTerrestre):
    pass


for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(cls1, cls2), end="\t")
    print()
