# criar função que duplique, triplique e quadriplique o número recebido como parâmetro

def multiplicacao(numero):
    def duplicar():
        return numero * 2
    def triplicar():
        return numero * 3
    def quadruplicar():
        return numero * 4
    
    return {
        'duplicar': duplicar,
        'triplicar': triplicar,
        'quadruplicar': quadruplicar
    }

multiplicacao_1 = multiplicacao(6)
multiplicacao_2 = multiplicacao(8)

print(multiplicacao_1['duplicar']())
print(multiplicacao_1['triplicar']())
print(multiplicacao_1['quadruplicar']())

print(multiplicacao_2['duplicar']())
print(multiplicacao_2['triplicar']())
print(multiplicacao_2['quadruplicar']())