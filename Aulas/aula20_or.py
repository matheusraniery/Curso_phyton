# Operador lógico OR

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Bem-vindo! ')
else:
    print('Senha incorreta ')

# Avaliação de curto circuito

# print(True or False) # sempre vai avaliar o primeiro valor verdadeiro.

# senha = input('Senha: ') or 'Sem senha'
# print(senha)
 