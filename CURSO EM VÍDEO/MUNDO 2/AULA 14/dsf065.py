'''
Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.
'''
cont = menor = maior = 0
tot = []
p = 'S'

while p == 'S':
  
  n = int(input('Digite um número: '))
  tot.append(n)
  cont += 1
  if cont == 1:
    maior = menor = n
  else:
    if n >= maior:
      maior = n
    elif n <= menor:
      menor = n
  p = str(input('Deseja continuar? [S/N]')).strip().upper()

med = sum(tot) // cont

print(f'Foi registrado que o menor número digitado foi {menor}.\nO maior número foi {maior}.\nE a média de todos os números é {med}.')