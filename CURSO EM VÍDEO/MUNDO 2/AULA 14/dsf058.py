'''
Melhore o jogo do desafio 028 onde o computador vai "Pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites 
foram necessários para vencer.
'''
from random import randint

print('Vamos jogar de Adivinhar?\nO computador irá gerar um número, e você tem que acertar para ganhar!')
n1 = randint(0, 10)
tent = 0
acertou = False

while not acertou:
  n2 = int(input('Escolha um número de 0 a 10: '))
  tent += 1
  if n1 == n2:
    acertou = True
  else:
    if n2 < n1:
      print('Mais... Tente novamente! ')
    elif n2 > n1:
      print('Menos... Tente novamente! ')

print(f'Parabéns, você acertou!!\nO número escolhido foi {n1}!')
print(f'Foram necessários {tent} tentativas para acertar.')