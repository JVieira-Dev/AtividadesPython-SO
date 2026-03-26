valor = int(input("Digite um número inteiro: "))

if valor % 2 == 0 and valor % 3 == 0:
    print("O número é divisível por 2 e por 3.")
elif valor % 2 == 0:
    print("O número é divisível por 2.")
elif valor % 3 == 0:
    print("O número é divisível por 3.")
else:
    print("O número não é divisível por 2 nem por 3.")