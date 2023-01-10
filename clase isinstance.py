class Vehiculo:
    pass


class VehiculoTerrestre(Vehiculo):
    pass


class VehiculoOruga(VehiculoTerrestre):
    pass


miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()

for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
    for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, cls), end="\t")
    print()
