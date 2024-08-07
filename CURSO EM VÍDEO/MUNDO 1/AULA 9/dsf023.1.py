'''faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados

ex: Digite um número: 1834
unidade: 4 
dezena: 3
centena: 8
milhar 1
'''
num = (input('Digite um número de 0 a 9999: '))
print(f'unidade: {num[3]}\ndezena: {num[2]}\ncentena: {num[1]}\nmilhar: {num[0]}')
