cadena = "Hola"

try:
    x = int(cadena)
except Exception as err:
    print("error", err)

print("He llegado al final")