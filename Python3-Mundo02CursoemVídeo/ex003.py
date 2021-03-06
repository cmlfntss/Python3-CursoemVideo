print("""Escreva um programa em Python que leia um número inteiro qualquer e peça para o 
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.""")

num = int(input('Digite um número:'))
print("""Escolha uma das opções abaixo:
[1] para BINÁRIO
[2] PARA OCTAL
[3] PARA HEXADECIMAL""")
opcao = int(input('Sua opção escolhida:'))
if opcao == 1:
    print('O valor em BINÁRIO é {}'.format(bin(num)))
elif opcao == 2:
    print('O valor em OCTAL é {}'.format(oct(num)))
elif opcao == 3:
    print('O valor em HEXADECIMAL é {}'.format(hex(num)))
else:
    print('Opção digitada INVÁLIDA!')

