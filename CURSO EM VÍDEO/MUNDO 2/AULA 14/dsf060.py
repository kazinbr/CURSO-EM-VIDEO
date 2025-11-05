'''
Faça um programa que leia um número qualquer
e mostre o seu fatorial
Ex: 5! = 5x4x3x2x1 = 120
'''

n = int(input('Escolha um número para ser fatorado: '))
res = 1
c = n

print(f'Calculando {n}! = ', end='')
while c > 0:
  print(f'{c}', end='')
  print(' x ' if c > 1 else ' = ', end='')
  res *= c
  c -= 1
  
print(f'{res}')