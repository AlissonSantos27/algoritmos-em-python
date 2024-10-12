n = int(input())

print(f"{n}")

# Contando cédulas de 100
cedulas100 = int(n / 100)
n = n - (cedulas100 * 100)

# Contando cédulas de 50
cedulas50 = int(n / 50)
n = n - (cedulas50 * 50)

# Contando cédulas de 20
cedulas20 = int(n / 20)
n = n - (cedulas20 * 20)

# Contando cédulas de 10
cedulas10 = int(n / 10)
n = n - (cedulas10 * 10)

# Contando cédulas de 5
cedulas5 = int(n / 5)
n = n - (cedulas5 * 5)

# Contando cédulas de 2
cedulas2 = int(n / 2)

cedulas1 = n - (cedulas2 * 2)

print(f"{cedulas100} nota(s) de R$ 100,00")
print(f"{cedulas50} nota(s) de R$ 50,00")
print(f"{cedulas20} nota(s) de R$ 20,00")
print(f"{cedulas10} nota(s) de R$ 10,00")
print(f"{cedulas5} nota(s) de R$ 5,00")
print(f"{cedulas2} nota(s) de R$ 2,00")
print(f"{cedulas1} nota(s) de R$ 1,00")