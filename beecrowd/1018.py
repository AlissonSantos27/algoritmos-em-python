"""
leia n

escreva n

se n >= 100 faça
    cedulas100 := int(n / 100)
fimse

n = n - (cedulas100 * 100)

se n >= 50 faça
    cedulas50 := int(n / 50)
fimse

n = n - (cedulas50 * 50)

se n >= 20 faça
    cedulas20 := int(n / 20)
fimse

n = n - (cedulas20 * 20)

se n >= 10 faça
    cedulas10 := int(n / 10)
fimse

n = n - (cedulas10 * 10)

se n >= 5 faça
    cedulas5 := int(n / 5)
fimse

n = n - (cedulas5 * 5)

se n >= 2 faça
    cedulas2 := int(n / 2)
fimse

cedulas1 = n - (cedulas2 * 2)

escreva cedulas100, "nota(s) de R$ 100,00"
escreva cedulas50, "nota(s) de R$ 50,00"
escreva cedulas20, "nota(s) de R$ 20,00"
escreva cedulas10, "nota(s) de R$ 10,00"
escreva cedulas5, "nota(s) de R$ 5,00"
escreva cedulas2, "nota(s) de R$ 2,00"
escreva n, "nota(s) de R$ 1,00"
"""

n = int(input())

print(f"{n}")

# Contando as notas de 100
if n >= 100:
    cedulas100 = int(n / 100)

# O valor que restou para contar depois de contar as notas de 100
n = n - (cedulas100 * 100)

# Contando as notas de 50
if n >= 50:
    cedulas50 = int(n / 50)

# O valor que restou para contar depois de contar as notas de 50
n = n - (cedulas100 * 50)

# Contando as notas de 20
if n >= 20:
    cedulas20 = int(n / 20)

# O valor que restou para contar depois de contar as notas de 20
n = n - (cedulas20 * 20)

# Contando as notas de 10
if n >= 10:
    cedulas10 = int(n / 10)

# O valor que restou para contar depois de contar as notas de 10
n = n - (cedulas10 * 10)

# Contando as notas de 5
if n >= 5:
    cedulas5 = int(n / 5)

# O valor que restou para contar depois de contar as notas de 5
n = n - (cedulas5 * 5)

# Contando as notas de 2
if n >= 2:
    cedulas2 = int(n / 2)

# cedulas de 1
cedulas1 = n - (cedulas2 * 2)

print(f"{cedulas100:.2f} nota(s) de R$ 100,00")
print(f"{cedulas50:.2f} nota(s) de R$ 50,00")
print(f"{cedulas20:.2f} nota(s) de R$ 20,00")
print(f"{cedulas10:.2f} nota(s) de R$ 10,00")
print(f"{cedulas5:.2f} nota(s) de R$ 5,00")
print(f"{cedulas2:.2f} nota(s) de R$ 2,00")
print(f"{cedulas1:.2f} nota(s) de R$ 1,00")