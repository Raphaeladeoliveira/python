print('Tabela de preços')
prod = float(input('Digite o preço do produto: '))
porc = prod * 10 / 100
desc = prod - porc
print('O valor a ser descontado do produto é {}, sendo assim com 10% de desconto fica {}'.format(porc, desc))