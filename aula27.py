# testando append, pop, del, e clear
lista = [10, 20, 30, 40]
lista[2] = 300
del lista[1]
print(lista)
lista.append(50)
lista.pop()
lista.append(55)
lista.append(65)
ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)

lista.append('Thalys')
# nome = lista.pop()
lista.append(123)
del lista[1]
# lista.clear()
lista.insert(2, 400)
print(lista)