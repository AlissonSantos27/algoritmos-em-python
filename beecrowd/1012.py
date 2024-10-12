PI = 3.14159

entrada = input()

valores = entrada.split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

#Área do triângulo retângulo que tem a como base e c por altura
triangulo = (a * c) / 2

#Área do círculo de raio c
circulo = PI * c ** 2

# Área do trapézio que tem a e b por bases e c por altura
trapezio = ((a + b) * c) / 2

# Área do quadrado que tem lado b
quadrado = b ** 2

# Área do retângulo que tem lados a e b
retangulo = a * b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")