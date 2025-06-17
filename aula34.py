string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, u = lista # para retonar o último ou ante penúltimo valor da lista
print(a, u)

print(*lista) # retorna a lista completa separadamente
print(*string) # também retorna a string
print(*tupla) # mesma coisa
