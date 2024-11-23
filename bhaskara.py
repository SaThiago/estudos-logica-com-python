import math
a=float(input("Coeficiente a "))
b=float(input("Coeficiente b "))
c=float(input("Coeficiente c "))

delta = b**2 - (4*a*c)

if delta >= 0:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)

else:
    print("esta equação não possui raízes reais")

if delta > 0 and raiz1 > raiz2:
    print("as raízes da equação são", raiz2, "e", raiz1)

if delta > 0 and raiz1 < raiz2:
    print("as raízes da equação são", raiz1, "e", raiz2)

if delta == 0:
    print("a raíz desta equação é", raiz1)


