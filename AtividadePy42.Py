soma = 0
denominador = 1
for numerador in range(1, 51):
    soma += numerador / denominador
    denominador += 2

print(f"Resultado da série: {soma:.4f}")