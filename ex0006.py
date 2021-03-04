n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}'.format(s))
print('A multiplicação entre {} e {} vale {}'.format(n1,n2,m))
print('A divisão entre {} e {} vale {:.2f}'.format(n1,n2,d))
print('A subtração entre {} e {} vale {}'.format(n1,n2,sub))
print('A divisão inteira entre {} e {} vale {}'.format(n1,n2,di))
print('A exponenciação entre {} e {} vale {}'.format(n1,n2,e))