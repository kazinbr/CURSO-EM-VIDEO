'''
Faça um programa que leia um número qualquer
e mostre o seu fatorial
Ex: 5! = 5x4x3x2x1 = 120
'''

n = int(input('Escolha um número para ser fatorado: '))
res = 1

original_n = n

while n > 1:
  res *= n
  n -= 1
  
print(f'O fatorial de {original_n}! é {res}')