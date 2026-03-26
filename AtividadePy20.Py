import math

a = float(input("Digite A: "))
b = float(input("Digite B: "))
c = float(input("Digite C: "))

if a == 0:
    print("Não é uma equação de segundo grau.")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Raiz única: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raízes: X1 = {x1} e X2 = {x2}")