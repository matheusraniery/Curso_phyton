'''
Introdução ao try/except
try -> tentar executar código
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print(f'Isso não é um número. ')


# if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#    print(f'Isso não é um número. ')