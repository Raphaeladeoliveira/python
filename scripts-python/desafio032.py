print('Fim de ano')
print('-----------')
notaa = float(input('Primeira nota' ))
notab = float(input('segunda nota: '))
notac = float(input('terceira: '))
notad = float(input('por fim a quarta: '))

calc = (notaa + notab + notac + notad) / 4

if(calc >= 7) :
    print('Aprovado! sua media foi de {}'.format(calc))
elif(calc < 7 and calc > 5):
    print('Recuperação! sua nota foi de {}'.format(calc))
else :
    print('Reprovado! sua nota foi de {}'.format(calc))
