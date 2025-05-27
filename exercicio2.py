numeroint = int(input('Digite um número inteiro: ')) # poderia ter usado numeroint.isdigit()
if numeroint % 2 == 0:
    print('O número é par')
elif numeroint % 2 <= 1:
    print('O número é impar')
else:
    print('Esse não é um número inteiro')


horasint = int(input('que horas são? '))
if horasint < 11:
    print('Bom dia')
elif horasint >= 12 and horasint < 17:
    print('Boa tarde')
else:
    print('Boa noite')

nomepedido = input('Digite o seu nome: ')
caracteres = len(nomepedido)

if caracteres <= 4:
    print('seu nome é curto')
elif caracteres == 5 or caracteres == 6:
    print('seu nome está na média')
else:
    print('seu nome é grande')