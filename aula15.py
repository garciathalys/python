nome = 'Thalys'
preco = 984.24
variavel = '%s, o valor é R$%.2f' % (nome, preco)
print(variavel)


variavel = 'Thalys'
print(f'{variavel}')
print(f'{variavel: >15}')
print(f'{variavel:c<10}')
