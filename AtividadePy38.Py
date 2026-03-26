maior = -1
menor = float('inf')

for i in range(100):
    num = float(input(f"Digite o {i+1}º número (positivo): "))
    if num > 0:
        if num > maior: maior = num
        if num < menor: menor = num

print(f"Maior: {maior} | Menor: {menor}")