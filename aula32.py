# split e join
# split divide uma string
# join une uma string

frase = 'Olha que coisa,    isso é interessante   '
lista_frase_cruas = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_cruas):
    lista_frase.append(lista_frase_cruas[i].strip()) # strip serve para cortar espaço na string
print(lista_frase_cruas)
print(lista_frase)

frases_unidas = '-'.join(lista_frase) # join une uma string, serve apenas para iteráveis
print(frases_unidas)