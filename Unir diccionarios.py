d1 = {"Adam Smith": "A", "Judy Paxton": "B+"}
d2 = {"Mary Louis": "A", "Patrick White": "C"}
d3 = {}

for item in (d1, d2):
    if d1.items() not in d2.items():
        d3.update(d1)
        d3.update(d2)


print(d3)


# Otra forma


d1 = {"Adam Smith": "A", "Judy Paxton": "B+"}
d2 = {"Mary Louis": "A", "Patrick White": "C"}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
