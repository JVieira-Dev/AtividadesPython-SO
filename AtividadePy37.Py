n = int(input("Digite quantos termos de Fibonacci deseja gerar: "))
a, b = 0, 1
cont = 0

while cont < n:
    print(a, end=" ")
    a, b = b, a + b
    cont += 1