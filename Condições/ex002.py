print("""---Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para 
o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.---""")

from random import randint
computador = randint(0, 5) #Computador pensando
print('-=-' * 25)
print('Pensando em um número entre 0 e 5, tente adivinhar!')
print('-=-' * 25)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Você acertou, PARABÉÉNS!!')
else:
    print('Você ERROU! O número que pensei foi {} e o que você escolheu foi o {}'.format(computador, jogador))