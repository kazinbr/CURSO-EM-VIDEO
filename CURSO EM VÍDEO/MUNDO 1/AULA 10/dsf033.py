'''
Faça um programa que leia três números e mostre qual é o maior 
e qual é o menor.
'''
n1 = int(input('Escolha seu primeiro número: '))
n2 = int(input('Escolha seu segundo número: '))
n3 = int(input('Escolha seu terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print(f'O maior número entre os três escolhidos é {n1}')
    else:
         print(f'O maior número entre os três escolhidos é {n3}')
else:
    if n2 > n3:
         print(f'O maior número entre os três escolhidos é {n2}')
    else:
        print(f'O maior número entre os três escolhidos é {n3}')
