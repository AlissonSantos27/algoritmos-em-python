import math
# DISTÂNCIA ENTRE DOIS PONTOS

ponto1 = input()
ponto2 = input()

p1 = ponto1.split()
p2 = ponto2.split()
# coordenadas do ponto 1
x1 = float(p1[0])
y1 = float(p1[1])
# coordenadas do ponto2
x2 = float(p2[0])
y2 = float(p2[1])

distancia = float(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))

print(f"{distancia:.4f}")