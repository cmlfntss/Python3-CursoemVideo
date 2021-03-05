print(' Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.')
nome = str(input('Digite o seu nome: '))
print('O nome digitado foi {} e a informação é {}.'.format(nome,'Silva' in nome.lower()))
