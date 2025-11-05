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
from time import sleep
resp = 0
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
print('=-=' * 10)

while resp != 5:
  print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
  resp = int(input('>>>>> Qual a sua opção? '))
  
  if resp == 1:
    print(f'{n1} + {n2} = {n1 + n2}.')
  elif resp == 2:
    print(f'{n1} X {n2} = {n1 * n2}')
  elif resp == 3:
    maior = 0 
    if n1 > n2:
      maior = n1
    else:
      maior = n2
    print(f'O maior número entre {n1} e {n2} é {maior}')
  elif resp == 4:
    n1 = int(input('Escolha um número: '))
    n2 = int(input('Escolha outro número: '))
  elif resp == 5:
    print('Finalizando...')
  else:
    print('Opção inválida, tente novamente! ')
  print('=-=' * 10)
  sleep(2)
print('Programa finalizado, volte sempre! ')
