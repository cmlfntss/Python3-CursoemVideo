#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

import math

catopos = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))

hi = (catopos ** 2 + catadj ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))