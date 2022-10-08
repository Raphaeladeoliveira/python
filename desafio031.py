print('Bem vindo ao alistamento')
print('************************')
nome = input('Seu nome por favor: ')
ano = int(input('Digite o ano do seu nascimento: '))
calc = 2022 - ano
idade = 18
if(calc < idade) :
    print('Você ainda não estar no tempo aguarde mais {} anos'.format(idade - calc))
elif (calc == idade) :
    print('Você ja está pronto pra se alistar {}!'.format(nome))
else :
    print('Infelizmente vocé é um fanfarão desatento {}'.format(nome))
    print('Já se passaram {} anos e você não fez seu alistamento'.format(calc - idade))


