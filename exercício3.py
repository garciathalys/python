nome = input('Digite o seu nome: ')
if not nome:
    print('desculpe, você deixou campos vazios')
    exit()
idade = input('Digite a sua idade: ')
if not idade:
    print('desculpe, você precisa digitar algo na idade')
    exit()
else:
    print(f'o seu nome é {nome}')
    print('o seu nome invertido é', nome[ : : -1])
    print('o seu nome tem', len(nome), 'letras')
    print('a primeira letra do seu nome é', nome[0])
    print('a última letra do seu nome é', nome[-1])

