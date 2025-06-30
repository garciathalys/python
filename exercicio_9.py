# gerando o primeiro dígito do cpf
# CPF: 746.824.890.70
# 7  4  6  8  2  4  8  9  0 
#10  9  8  7  6  5  4  3  2
#70  36  48 56 12 20 32 27 = 301 * 10 = 3010
# 

cpf = '74682489070'
nove = cpf[0:9]
contador = 10

resultado = 0
for digito in nove:
    resultado += int(digito) * contador
    contador -= 1
primeiro = (resultado * 10) % 11
primeiro = primeiro if primeiro <= 9 else 0
print(primeiro)