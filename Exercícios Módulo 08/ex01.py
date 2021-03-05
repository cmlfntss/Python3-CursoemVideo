#Crie um programa que leia um n[umero real qualquer pelo teclado
#e mostre na tela a sua porção inteira

from math import trunc
num = float(input('Digite um número qualquer: '))
print('O número {} tem a parte inteira igual {}'.format(num, trunc(num)))

