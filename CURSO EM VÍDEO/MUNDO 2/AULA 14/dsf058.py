'''
Melhore o jogo do desafio 028 onde o computador vai "Pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.
'''
from random import randint

print('Vamos jogar de Adivinhar?\nO computador irá gerar um número, e você tem que acertar para ganhar!')

n1 = randint(0, 10)
n2 = int(input('Escolha um número: '))
tent = 0

while n2 != n1:
  n2 = int(input('Você errou!\nTente novamente e escolha outro número: '))
  tent += 1

print(f'Parabéns, você acertou!!\nO número escolhido foi {n1}!')
print(f'Foram necessários {tent} tentativas para acertar.')