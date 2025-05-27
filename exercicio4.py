nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)
print(f'O seu nome tem {tamanho_nome} letras')

while tamanho_nome <= 20:
    nova_string = f'{nome[:13]}EU SOU LINDO'
    novo_tamanho_nome = len(nova_string)
    print(nova_string)
    if novo_tamanho_nome >= 15:
        break