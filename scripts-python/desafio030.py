print('============== Emprestimo ==============')
nome = input('Seu nome: ')
valorcasa = float(input('Digite o valor da casa em questão: '))
sala = float(input('Informe o valor do seu salario: '))
anos = int(input('Em quantos anos deseja pagar: '))
mes = (anos * 12)
prest = valorcasa / mes
salporc = (sala * 30)/100


if(prest < salporc) :
    print('olá {} suas parecelas ficaram em {} meses...'.format(nome, mes))
    print('no valor de {}'.format(prest))
else :
    print('Infelizmente sua renda não condiz com o desejado...')
