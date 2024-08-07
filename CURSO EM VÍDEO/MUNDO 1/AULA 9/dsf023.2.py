'''faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados

ex: Digite um número: 1834
unidade: 4 
dezena: 3
centena: 8
milhar 1
'''
num = int(input('Digite um valor entre 0 a 9999: '))
unidade = num%10
print(f'unidade: {unidade}')
num //= 10

dezena = num%10
print(f'dezena: {dezena}')
num //= 10

centena = num%10
print(f'centena: {centena}')
num //= 10

milhar = num%10
print(f'milhar: {milhar}')
