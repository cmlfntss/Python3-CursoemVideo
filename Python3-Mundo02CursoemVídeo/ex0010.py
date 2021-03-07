sintoma = int(input("""Informe se vc está sentindo um dos sintomas:
[1] TOSSE
[2] NÃO SENTE O GOSTO DOS ALIMENTOS OU CHEIRO
[3] DOR NO CORPO
[4] TODOS OS SINTOMAS\n"""))
if sintoma == 1:
   print('Como você ainda sente apenas um dos sintomas e digitou a opção {}, aguarde e vá se cuidando.'.format(sintoma))
elif sintoma == 2:
    print('Como você ainda sente apenas um dos sintomas e digitou a opção {}, aguarde e vá se cuidando. '.format(sintoma))
elif sintoma == 3:
    print('Como você ainda sente apenas um dos sintomas e digitou a opção {}, aguarde e vá se cuidando. '.format(sintoma))
elif sintoma == 4:
    print('Melhor você correr para realizar um exame de COVID, pois você selecionou a opção {}'.format(sintoma))
else:
    print('Você não escolheu uma das opções, então não está com sintomas de COVID, se cuida e não esquece o ÁLCOOL EM GEL!!!!')