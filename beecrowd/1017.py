tempo = int(input())
velocidade = int(input())

# vm = espaço / tempo
# espaço = vm * tempo

distancia = velocidade * tempo

combustivel = distancia / 12

print(f"{combustivel:.3f}")