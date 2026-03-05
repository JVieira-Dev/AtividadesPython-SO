tempoPercurso = float(input("Digite o tempo gasto no percurso (em horas): "))
velocidadeMedia = float(input("Digite a velocidade média do percurso (em km/h): "))

litrosGastos = (tempoPercurso * velocidadeMedia) / 12

print("A quantidade de litros gastos no percurso é de: ", litrosGastos, "L")