n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6.0:
    print("Média {media}: APROVADO")
elif media >= 3.0:
    print("Média {media}: EXAME")
else:
    print("Média {media}: RETIDO")