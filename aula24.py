#  Operadores in e not in
#  Strings são iteráveis
#  0  1  2  3  4 
#  T  h  a  i  s 
# -5 -4 -3 -2 -1
#nome = 'Thais'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digete seu nome: ')
encontrar = input('Digete o que deseja encontrar: ')

if encontrar in nome: 
    print(f'{encontrar} esta em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')

