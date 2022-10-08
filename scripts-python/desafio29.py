import emoji
velocidade = int(input('Qual a velocidade: '))

multa = (velocidade - 80) * 7
if (velocidade > 80) :
    print('Você excedeu o limite de velocidade, você será multado no valor de {}R$'.format(multa))
else :
    print(emoji.emojize('Siga em frente motorista consciente sem multa :thumbs_up:'))