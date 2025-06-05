# teste copiando valores mutáveis
lista_a = ['Thalys', 'Clara', 1, True, 1.2]
lista_b = lista_a 
#lista_b = lista_a.copy()
lista_a[0] = 'Macarrão'
print(lista_a)
print(lista_b)