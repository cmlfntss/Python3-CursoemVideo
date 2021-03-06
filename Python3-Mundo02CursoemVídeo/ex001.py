nome = str(input('Qual seu nome? '))
if nome == 'Camila':
    print('Que nome bonito!')
elif nome == 'Celma' or nome == 'Thalita' or nome == 'Paulo':
    print('O seu nome é {}, belíssimo, tenha um bom dia!'.format(nome))
else:
    print('Seu nome é normal, tenha um bom dia {}!'.format(nome))