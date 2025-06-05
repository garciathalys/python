for i in range(10):
    if i == 5:
        print('i é 5, pulando...')
        continue
    if i == 9:
        print('i é 9, seu else não será executado')
        break
    for j in range(1,3):
        print(i, j)
else:
    print('for completo com sucesso')