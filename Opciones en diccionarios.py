# BUSCAR EN EL DICCIONARIO

pol_esp_dictionary = {"kwiat": "flor", "woda": "agua", "gleba": "tierra"}

item_1 = pol_esp_dictionary["gleba"]  # Ejemplo 1.
print(item_1)  # salida: tierra

item_2 = pol_esp_dictionary.get("woda")  # Ejemplo 2.
print(item_2)  # salida: agua


# CAMBIAR EL VALOR A UNA CLAVE


pol_esp_dictionary = {"zamek": "castillo", "woda": "agua", "gleba": "tierra"}

pol_esp_dictionary["zamek"] = "cerradura"
item = pol_esp_dictionary["zamek"]
print(item)  # salida: cerradura

pol_esp_dictionary = {"zamek": "castillo", "woda": "agua", "gleba": "tierra"}

pol_esp_dictionary["zamek"] = "cerradura"
item = pol_esp_dictionary["zamek"]
print(item)  # salida: cerradura


# AGREGAR O ELIMINAR CLAVE

phonebook = {}  # un diccionario vacío

phonebook["Adán"] = 3456783958  # crear/agregar un par clave-valor
print(phonebook)  # salida: {'Adán': 3456783958}

del phonebook["Adán"]
print(phonebook)  # salida: {}

phonebook = {}  # un diccionario vacío

phonebook["Adán"] = 3456783958  # crear/agregar un par clave-valor
print(phonebook)  # salida: {'Adán': 3456783958}

del phonebook["Adán"]
print(phonebook)  # salida: {}


# INSERTAR ELEMENTO

pol_esp_dictionary = {"kwiat": "flor"}

pol_esp_dictionary.update({"gleba": "tierra"})
print(pol_esp_dictionary)  # salida: {'kwiat': 'flor', 'gleba': 'tierra'}

pol_esp_dictionary.popitem()
print(pol_esp_dictionary)  # salida: {'kwiat': 'flor'}

pol_esp_dictionary = {"kwiat": "flor"}

pol_esp_dictionary.update({"gleba": "tierra"})
print(pol_esp_dictionary)  # salida: {'kwiat': 'flor', 'gleba': 'tierra'}

pol_esp_dictionary.popitem()
print(pol_esp_dictionary)  # salida: {'kwiat': 'flor'}


# USAR BUCLE FOR PARA ITERAR

pol_esp_dictionary = {"zamek": "castillo", "woda": "agua", "gleba": "tierra"}

for item in pol_esp_dictionary:
    print(item)

# salida: zamek
#         woda
#         gleba

pol_esp_dictionary = {"zamek": "castillo", "woda": "agua", "gleba": "tierra"}

for item in pol_esp_dictionary:
    print(item)

# salida: zamek
#         woda
#         gleba
