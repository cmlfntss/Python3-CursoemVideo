#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o valor do seu salário atual: "))
aumento = salario + (salario * 15 / 100)

print('O valor do seu salário atual é de {:.2f} com o aumento de 15% o valor atual é de {:.2f} '. format(salario, aumento))