entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input ('Senha: ')
senha_permitida = 'senha123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Logado')
else:
    print('Não foi possível logar')