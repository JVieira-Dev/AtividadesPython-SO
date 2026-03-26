hi = int(input("Hora inicial: "))
mi = int(input("Minuto inicial: "))
hf = int(input("Hora final: "))
mf = int(input("Minuto final: "))

inicio_min = hi * 60 + mi
fim_min = hf * 60 + mf

if fim_min <= inicio_min:
    duracao = (1440 - inicio_min) + fim_min
else:
    duracao = fim_min - inicio_min

h_total = duracao // 60
m_total = duracao % 60

print(f"Duração total: {h_total} horas e {m_total} minutos.")