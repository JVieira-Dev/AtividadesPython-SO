base = int(input("Base: "))
expoente = int(input("Expoente: "))
resultado = 1

for _ in range(expoente):
    resultado *= base

print(f"Resultado: {resultado}")