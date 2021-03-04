#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input("Qual é o valor do seu produto? "))
desc = produto - (produto * 5 / 100)
print("O valor do seu produto é de R${:.2f} com o desconto de 5% o novo valor é R${:.2f}" .format(produto, desc))