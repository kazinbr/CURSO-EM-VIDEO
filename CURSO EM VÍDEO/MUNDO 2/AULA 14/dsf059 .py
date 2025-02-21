'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em
cada caso
'''
resp = 0
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))

while resp != 5:
  print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
  resp = int(input('Escolha o que deseja fazer com os valores informados: '))
  
  if resp == 1:
    print(f'{n1} + {n2} = {n1 + n2}.')
  if resp == 2:
    print(f'{n1} X {n2} = {n1 * n2}')
  if resp == 3:
    maior = 0 
    if n1 > n2:
      maior = n1
    else:
      maior = n2
    print(f'O maior número entre {n1} e {n2} é {maior}')
  if resp == 4:
    n1 = int(input('Escolha um número: '))
    n2 = int(input('Escolha outro número: '))
