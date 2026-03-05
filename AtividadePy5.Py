A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

delta = (B ** 2) - (4 * A * C)

RaizDelta = delta ** 0.5
x1 = (-B + RaizDelta) / (2 * A)
x2 = (-B - RaizDelta) / (2 * A)

print("As raízes da equação são:", x1, "e", x2)