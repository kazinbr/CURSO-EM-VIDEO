'''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

o programa deverá escrever na tela se o usuário venceu ou perdeu
'''
from random import randint
print('Vamos jogar de Adivinhar?\nO computador irá gerar um número, e você tem que acertar para ganhar!')
n1 = randint(0, 5)
n2 = int(input('Escolha um número: '))

if n2 == n1:
    print(f'Você acertou!! O número adivinhado é {n1}')
else:
    print(f'Você perdeu!! O número correto é {n1} :( ')
