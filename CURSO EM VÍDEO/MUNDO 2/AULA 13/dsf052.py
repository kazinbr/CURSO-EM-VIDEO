'''
Faça um programa que leia um número inteiro e diga se ele é
ou não um número primo.
'''

primo = int(input('Digite um número: '))
tot = 0
for i in range(1, primo+1):
    if primo % i == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')

print(f'\n\033[mO número {primo} foi divisível {tot} vezes')

if tot == 2:
    print(f'O número {primo} é um número primo!!')
else:
    print(f'O número {primo} não é um número primo :(')