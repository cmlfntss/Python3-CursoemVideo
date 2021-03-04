#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite a informação que deseja visualizar: ')
print('O valor primitivo desse valor é {} '.format(n))
print('Qual é o tipo desta informação?',type(n))
print('É númerico?', n.isnumeric())
print('Só tem espaços?', n.isspace())
print('É alfabético?', n.isalpha())
print('Está em maiúsculas?', n.isupper())
print('Está em minúscula?', n.islower())
print('Está capitalizada?', n.istitle())

