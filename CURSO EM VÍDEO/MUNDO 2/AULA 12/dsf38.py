''' 
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}!!')
elif n2 > n1:
    print(f'o número {n2} é maior que o número {n1}')
else:
    print('Não existe número maior, ambos são iguas!!')
