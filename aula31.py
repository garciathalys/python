# testando o enumerate

lista = ['Thalys', 'Laura', 'Carol']
lista.append('João')

# lista_enumerada = list(enumerate(lista, start=10))

for item in enumerate(lista):
   print(item)

# for indice, nome in enumerate(lista):
#   print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#   print('FOR da tupla:')
#   for valor in tupla_enumerada:
#       print(f'\t{valor}')

#print(lista_enumerada)