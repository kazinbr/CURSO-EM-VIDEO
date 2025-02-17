'''
Crie um programa que leia o ano de nascimento de sete pessoas
. No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores

*Considerando 21 anos como maioridade*
'''

from datetime import date

atual = date.today().year

maiores = 0
menores = 0

for i in range(1, 8):
  nasc = int(input((f'Qual o ano do nascimento da {i}ª pessoa: ')))
  idade = atual - nasc

  if idade >= 21:
    maiores += 1
  else:
    menores += 1

print(f'No total, temos {maiores} pessoas maior de idade.')
print(f'E também tivemos {menores} pessoas menores de idade.')
