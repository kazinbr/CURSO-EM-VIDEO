'''
Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999 que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(considerando o flag)
'''

n = 0
cont = 0
tot = []

while n != 999:
  n = int(input('Digite um valor: '))
  tot.append(n)
  soma = sum(tot) - 999
  if n != 999:
    cont += 1

print(f'Você digitou {cont} números e a soma total deles deu: {soma}!')