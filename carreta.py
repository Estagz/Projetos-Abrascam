print('\033[34m-=\033[m'*16)
print('\033[1;31m          ABRASCAM\033[m')
print('Cálculo de Mensalidade Carretas')
print('\033[34m-=\033[m'*16)

bitrem = int(input('Digite \033[1;31m[1]\033[m Carreta Simples \n'
                   'Digite \033[1;31m[2]\033[m Bitrem '))

if bitrem == 1:
    carreta = float(input('Digite o valor da carreta: R$ '.strip()))
    if carreta < 50000:
        mens = carreta * 0.003 + 59
    if carreta >= 50000:
        mens = carreta * 0.003 + 59 + 55
    assist = int(input('Deseja Assistência?\n'
                       'Digite \033[1;31m[1]\033[m para SIM \n'
                       'Digite \033[1;31m[2]\033[m para NÃO '.strip()))

    if assist == 1:
        mens = mens + 50
    elif assist == 2:
        mens = mens
    print('O valor da mensalidade é \033[1;32mR$ {:.2f}\033[m.'.format(mens))
elif bitrem == 2:
    carreta = float(input('Digite o valor do bitrem (Valor Total): R$ '.strip()))
    if carreta / 2 < 50000:
        mens = carreta * 0.003 + 59 + 59
    if carreta / 2 >= 50000:
        mens = carreta * 0.003 + 59 + 59 + 55 + 55
    assist = int(input('Deseja Assistência?\n'
                       'Digite \033[31m[1]\033[m para SIM \n'
                       'Digite \033[31m[2]\033[m para NÃO '.strip()))

    if assist == 1:
        mens = mens + 50 + 50
    elif assist == 2:
        mens = mens
    print('O valor da mensalidade é \033[1;32mR$ {:.2f}\033[m.'.format(mens))
else:
    print('Opção Inválida.')
