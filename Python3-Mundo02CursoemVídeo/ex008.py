altura = float(input('Digite a sua altura:'))
peso = float(input('Digite o seu peso: '))

imc = peso / altura **2

print("Seu IMC é: %.1f" % imc)

if imc < 18.5:
    print('O seu IMC é {:.1f} e você está ABAIXO do peso!'.format(imc))
elif imc == 18.5 or imc < 25:
    print('O seu IMC é {:.1f} e você está com o peso IDEAL!'.format(imc))
elif imc <= 25 or imc == 30:
    print('O seu IMC é {:.1f} e você está com o peso IDEAL!'.format(imc))
else:
    print('O seu IMC é {:.1f} e você está com OBESIDADE MÓRBIDA!'.format(imc))
