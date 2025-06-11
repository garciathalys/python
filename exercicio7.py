lista = []
comandos = 'i', 'a', 'l', 's'
while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir  [a]pagar  [l]istar  [s]air: ')
    if opcao == 'i':
        item = input('Qual item você gostaria de adicionar à lista? ')
        lista.append(item)
        print('O item foi adicionado a lista com sucesso!')
    elif opcao == 'a':
        if not lista:
            print('A lista está vazia, nada para apagar.')
        else:
            print('Itens na lista: ')
            for idl, item in enumerate(lista):
                print(f'{idl}: {item}')
        apagar = input('Digite o nome do item que você quer apagar: ')
        if apagar in lista:
            lista.remove(apagar)
            print('O item foi removido com sucesso.')
        else:
            print(f'O item "{apagar}" não existe na lista.')
    elif opcao == 'l':
        print('Itens na lista: ')
        for idl, item in enumerate(lista):
            print(f'{idl}: {item}')
    elif opcao == 's':
        break