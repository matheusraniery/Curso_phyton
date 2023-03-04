# O CRLF é uma quebra de linha específica do windows.Chamado de \r\n -> CRLF
# O sep é utilizado como separador por exemplo: se estivesse sep=',' ele entederia 1,2,3 como está sep='-' ele entende 1-2-3.
# O end é utilizado par definir o final de linha.
print(1,2, 3,4, sep='-', end='\n')
print(5,6, 7,8, sep='-', end='\n')
print(9,10, 11,12, sep='-', end='\n')