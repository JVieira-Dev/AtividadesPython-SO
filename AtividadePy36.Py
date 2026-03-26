import math

n = int(input("Digite N: "))
serie = 1.0

for i in range(1, n + 1):
    serie += 1 / math.factorial(i)

print(f"O resultado da série é:", serie)