# Exercício 27: Velocidade Média no Circuito
voltas = int(input("Digite o número de voltas: "))
extensao_metros = float(input("Digite a extensão do circuito (em metros): "))
tempo_minutos = float(input("Digite o tempo de duração (em minutos): "))

distancia_total = (voltas * extensao_metros) / 1000

tempo_horas = tempo_minutos / 60

velocidade_media = distancia_total / tempo_horas

print("A velocidade média foi de", (velocidade_media.2), "km/h")