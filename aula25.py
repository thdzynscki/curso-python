"""
Interpolação básica de strings
s - string
d e i - not
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Thais'
preco = 1000.95896585
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))