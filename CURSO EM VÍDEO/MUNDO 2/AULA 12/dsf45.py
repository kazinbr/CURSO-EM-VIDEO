''' 
Crie um programa que faça o computador jogar Jokenpô com você
'''
import random 

jogo = input('Vamos jogar Jokenpô? Escolha Pedra, Papel ou Tesoura: ')
resp = jogo.upper()

mov = ['Pedra', 'Papel', 'Tesoura']

pc = random.choice(mov)
print(f'Eu escolho {pc}!')

respc = pc.upper()

if resp == 'PAPEL':
    if respc == 'PAPEL':
        print('Deu empate, vamos jogar novamente?')
    elif respc == 'TESOURA':
        print('Eu ganhei!! Quer tentar novamente?')
    elif respc == 'PEDRA':
        print('Você venceu!! irei ganhar na próxima, quer tentar novamente?')
elif resp == 'PEDRA':
    if respc == 'PAPEL':
        print('Eu ganhei!! Quer tentar novamente?')
    elif respc == 'TESOURA':
        print('Você venceu!! irei ganhar na próxima, quer tentar novamente?')
    elif respc == 'PEDRA':
        print('Deu empate, vamos jogar novamente?')
elif resp == 'TESOURA':
    if respc == 'PAPEL':
        print('Você venceu!! irei ganhar na próxima, quer tentar novamente?')
    elif respc == 'TESOURA':
        print('Deu empate, vamos jogar novamente?')
    elif respc == 'PEDRA':
        print('Eu ganhei!! Quer tentar novamente?')
else:
    print('Você está tentando roubar? Não vale tentar me enganar viu??\nTente novamente!')
