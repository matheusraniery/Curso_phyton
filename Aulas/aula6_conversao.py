# Conversão de tipo, coerção, type convertion, typecasting, coercion é o ato de converter um tipo em outro tipo imutáveis e primitivos:
# str, int, float, bool
print(type('1')) # Aqui será uma str
print(int('1'),type(int('1'))) # Aqui foi convertido para número inteiro.
# O python não soma str com número para que isso aconteça nesse exemplo:
# print('1'+ 1)
# Teria que transformar a str em int.
print(int('1') + 1)
# Um float com um inteiro ele retorna um outro float
print(float('1.2') + 1)
# Uma string vazia dentro de uma classe booleana é considerada False, ela precisa ter algum valor dentro mesmo que seja um espaço.
print(bool(''))
print(bool(' '))
# O + é usado tanto para somar quanto para concatenar
print(str(11)+ 'b' )