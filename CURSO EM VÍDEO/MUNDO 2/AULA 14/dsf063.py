'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma 
Sequencia de Fibonacci.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
'''
n = int(input('Escolha dois números para iniciar a Sequência de Fibonacci\nO primeiro: '))
n1 = int(input('O segundo: '))
n2 = int(input('Escolha quantos números você gostaria de ver na sequência: '))

print(f'{n} > {n1} > ', end='')

cont = 3
while cont <= n2:
  sf = n + n1
  print(f'{sf}', end=' > ')
  n = n1
  n1 = sf
  sf = n + n1
  cont += 1
print('Fim!')