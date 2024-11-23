import math

x1 = float(input("Coordenada X do primeiro ponto:"))
y1 = float(input("Coordenada Y do primeiro ponto:"))
x2 = float(input("Coordenada X do segundo ponto:"))
y2 = float(input("Coordenada Y do segundo ponto:"))

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if dist >= 10:
    print("longe")
else:
    print("perto")