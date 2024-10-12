entrada1 = input()
entrada2 = input()

peca1 = entrada1.split()
peca2 = entrada2.split()

qtd1 = float(peca1[1])
preco1 = float(peca1[2])

qtd2 = float(peca2[1])
preco2 = float(peca2[2])

total = (qtd1 * preco1) + (qtd2 * preco2)

print(f"VALOR A PAGAR: R$ {total:.2f}")