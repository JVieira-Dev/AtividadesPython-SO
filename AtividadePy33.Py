numeroInt = int(input("Digite um número: "))
soma = 0

for i in range(1, numeroInt + 1):
    soma += 1/i

print("O resultado da série é: ", soma)