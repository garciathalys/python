# funções em def e parâmetros

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Thalys')
saudacao('Carlos')
saudacao('Fernando')
saudacao()

# sempre que nomear um argumento, é preciso nomear todos os próximos

def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(x=1, y=2, z=5)

print(1, 2, 3, sep='-')