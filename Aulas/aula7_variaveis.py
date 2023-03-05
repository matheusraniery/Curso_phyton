# Variáveis são usadas para salvar algo na memória do computador.
# PEP8:; inicie variáveis com letras minúsculas, pode usar números e underline _.
# O sinalde = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável)
# Uso: nome_variavel = expressão

nome_completo = 'Matheus Raniery'
soma_um_mais_um = 1 + 1
numero_um = int('1')
print(nome_completo, soma_um_mais_um) # Ele vai printar a variável que puxei.
# Podemos usar variáveis para não ficar repetidas vezes usando o mesmo código
print(int('1'),type(int('1')))
# Logo ficaria assim com a variável
print(numero_um,type(numero_um))

nome = 'Matheus'
idade = 26
maior_de_idade = idade >= 18 # Aqui temos uma expressão jogada dentro de uma variável
print('Nome:', nome)
print('Idade:', idade)
print('É maior de idade?', maior_de_idade)