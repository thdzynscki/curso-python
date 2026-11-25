nome = 'Thais Drabezynscki'
altura = 1.70
peso = 80
imc = peso / (altura ** 2)

"f-strings"

linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é {imc}'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
