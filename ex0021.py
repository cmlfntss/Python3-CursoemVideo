#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
#R$60 por dia e R$0,15 por Km rodado.

dias = int (input("Digite a quantidade de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de KM percorridos com o carro: "))

diaria = (dias * 60) + (km * 0.15)



print('O valor total a pagar é {:.2f}'.format(diaria))



