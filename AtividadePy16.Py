horasTrabalhadas = int(input("Digite o número de horas trabalhadas: "))
valorHora = float(input("Digite o valor por hora trabalhada: "))
desconto = float(input("Digite o número equivalente ao percentual do desconto: "))
dependentes = int(input("Digite o número de dependentes: "))

salarioBruto = horasTrabalhadas * valorHora
salarioLiquido = salarioBruto - (salarioBruto * desconto / 100) + (dependentes * 100)

print("O salário líquido é: ", salarioLiquido)