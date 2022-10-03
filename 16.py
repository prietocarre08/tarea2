f = open("archivo.txt", "r")

print(f.readlines())

for line in f:
    print(line.strip())
    print(line.split())
    print(line[1])

f.write("manzana, 3, 4")

print(f.readlines())