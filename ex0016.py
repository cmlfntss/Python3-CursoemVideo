num = float(input("Quanto dinheiro você tem na carteira? "));
dolar = num / 5.57
print('Com R${:.2f} você pode comprar US${:.2f} '.format(num, dolar));