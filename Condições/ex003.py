print('-=-' * 25)
print("""Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.""")
print('-=-' * 25)
veloc = int(input('Digite a velocidade do seu carro: '))
if veloc <= 80:
    print('Você está dentro do limite permitido, atualmente sua velocidade é {}'.format(veloc))
else:
    multa = (veloc - 80) * 7
    print('Você está ACIMA do permitido e foi MULTADO, sendo assim a multa é de R${}, dirija com cuidado!'.format(multa))