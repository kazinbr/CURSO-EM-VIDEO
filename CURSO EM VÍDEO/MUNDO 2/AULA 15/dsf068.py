'''
Faça um programa que jogue par ou impar com o computador.
O jogo ó será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''
from random import randint

n = c = s = v = 0
p = ''
print ('=-='*10)
print('Vamos jogar Par ou Ímpar!')
print ('=-='*10)

while True: 
    p = input('Escolha Par ou Ímpar? [P/I]: ').upper().strip()
    n = int(input('Escolha um número: '))
    c = randint(0, 10)
    s = c + n
    print('---'*10)
    if s % 2 == 0:
        print(f'Você jogou {n} e o computador {c}. Total de {s}, DEU PAR')
    else:
        print(f'Você jogou {n} e o computador {c}. Total de {s}, DEU ÍMPAR')
    print('---'*10)
    if p == 'P':
        if s % 2 == 0:
            print ('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif p == 'I':
        if s % 2 == 0:
            print('Você PERDEU!')
            break
        else: print('Você VENCEU!')
    v += 1
    print('Vamo jogar novamente...')
    print('=-='*10)
print(f'Você perdeu com {v} vitórias consecutivas!')

    