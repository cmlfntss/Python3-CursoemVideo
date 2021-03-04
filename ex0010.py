#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite a distância em metros: '))

#c = distancia * 100

print('A medida convertida de metros para centímeros é igual a {:.0f}cm e em milímetros {:.0f}mm' .format(medida * 100, (medida * 1000)))

print ('A medida convertida em KM é igual a {:.2f} km '.format(medida * 0.001000))
print('A medida em DAM é igual a {} dam '.format(medida * 0.010))
print('A medida em HM é igual a {} hm'.format(medida * 0.0100))
print('A medida em DM é igual a {:.0f} dm '.format(medida/0.10))
