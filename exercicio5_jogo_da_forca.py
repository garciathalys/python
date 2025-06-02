# exercício para descobrir qual é a palavra, semelhante ao jogo da forca
palavra = 'comboio'
tentativas = 0
letras_certas = []

while True:
    resultado = ''
    for letra in palavra:
        if letra in letras_certas:
            resultado += letra        
        else:
            resultado += '*'
    print('Palavra: ', resultado)

    if resultado == palavra:
        print('Parabéns! Você acertou a palavra')
        break
    letra = input('Digite uma letra para descobrir se ela faz parte da palavra: ').lower()
    tentativas += 1
    print(f'Você já tentou {tentativas}x')

    if letra in letras_certas:
        print('Você já acertou essa letra.')
    elif letra in palavra:
        letras_certas.append(letra)
    else:
        print('A letra não está na palavra.')

    