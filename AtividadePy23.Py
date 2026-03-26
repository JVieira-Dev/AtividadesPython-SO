valor1 = int(input("Digite o menor número inteiro da sequência: "))
valor2 = int(input("Digite o número inteiro do meio da sequência: "))
valor3 = int(input("Digite o maior número inteiro da sequência: "))
valor4 = int(input("Digite um número inteiro aleatório: "))

if valor1 > valor2 > valor3:
    if valor4 < valor1:
        print(valor4,",",valor1,",",valor2,",",valor3)
    elif valor1 < valor4 < valor2:
        print(valor1,",",valor4,",",valor2,",",valor3)
    elif valor2 < valor4 < valor3:
        print(valor1,",",valor2,",",valor4,",",valor3)
    else:
        print(valor1,",",valor2,",",valor3,",",valor4)