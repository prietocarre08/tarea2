numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros.append(10)
numeros.remove(6)
numeros.pop(6)

print(numeros)
print(numeros[-1])
print(10 in numeros)

numeros.sort()
numeros.reverse()

print(numeros)

for elem in numeros:
    print(elem)

for i in range(len(numeros)):
    print(numeros[i])

cadena = "Hola Mundo"

for c in cadena:
    print(c)

frutas = "Durazno, manzana, papaya"

print(frutas.split(","))