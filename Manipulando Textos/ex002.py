print("""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.""")

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('O seu primeiro nome tem {} letras '.format(nome.find(' ')))
print('O seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print(separa)