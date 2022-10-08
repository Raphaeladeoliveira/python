from random import randint
import emoji
comp = randint(0,5) #faz o computador pensar
jog = int(input('Em que número eu pensei?: '))



if(jog == comp) :
    print('Eu pensei em {} Parabéns Voce acertou! '.format(comp))
else:
    print('Você errou, Eu ganhei!! pensei em {} '.format(comp))













