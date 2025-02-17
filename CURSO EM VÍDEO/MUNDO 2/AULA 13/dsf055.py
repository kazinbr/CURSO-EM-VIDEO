'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
o maior e o menor peso lidos.
'''

for i in range(1, 6):
  peso = float(int(f'Digite o peso da {i}ª pessoa: '))

  if i == 1:
    maior = peso
    menor = peso
else:
  if peso > maior:
    maior = peso
  if peso < menor:
    menor = peso

print(f'O maior peso lido foi{}')