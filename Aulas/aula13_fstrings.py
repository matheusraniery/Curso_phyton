# Introdução a formatação de strings

nome = input('Digite o nome:')
altura = float(input('Digite a altura:'))
peso = float(input('Digite o peso:'))
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu imc é {imc:.2f}'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
 