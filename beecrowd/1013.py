n = input()

valores = n.split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maiorAB = (a + b + abs(a - b)) // 2 # a variável recebe o maior entre A e B

maiorABC = (maiorAB + c + abs(maiorAB - c)) // 2 # a variável recebe o maior entre maiorAB e C

print(f"{maiorABC} eh maior")