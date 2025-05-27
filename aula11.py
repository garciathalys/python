primeiro_valor = int(input('digite um valor: '))
segundo_valor = int(input('digite outro valor, por favor: '))
if segundo_valor > primeiro_valor:
    print('o segundo valor é maior do que o primeiro')
elif primeiro_valor > segundo_valor:
    print('o primeiro valor é maior do que o segundo')
else:
    print('os valores são iguais')
