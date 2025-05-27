contador = 0
while contador <= 50:
    contador += 2

    if contador == 24:
        print('Sem mostrar o número 24')
        continue

    print(contador)

    if contador == 30:
        break