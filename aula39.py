# closure e funções retornando funções

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar


saudacao1 = criar_saudacao('Bom dia', 'Thalys')
saudacao2 = criar_saudacao('Boa noite', 'Willian')

print(saudacao1())
print(saudacao2())
