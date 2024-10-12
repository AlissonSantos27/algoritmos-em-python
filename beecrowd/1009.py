nome = input()
salario = float(input())
vendasTotais = float(input())

total = (vendasTotais * 0.15) + salario

print(f"TOTAL = R$ {total:.2f}")