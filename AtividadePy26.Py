valor1 = int(input("Digite um número inteiro: "))
valor2 = int(input("Digite outro número inteiro: "))

if valor1 > valor2 & valor1 % valor2 == 0:
    print("{valor1} é múltiplo de {valor2}.")
elif valor2 > valor1 & valor2 % valor1 == 0:
    print("{valor2} é múltiplo de {valor1}.")
else:
    print("Nenhum dos números é múltiplo do outro.")