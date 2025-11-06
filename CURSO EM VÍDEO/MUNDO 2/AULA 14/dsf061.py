'''
Refaça o desaio 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando uma estrutura while
'''
print('Gerador de PA')
print('-=-' * 10)

termo = int(input('Escolha o termo da PA: '))
razao = int(input('Escolha a razão de sua PA: '))
cont = 1

while cont <= 10:
  print(f'{termo} > ', end='')
  termo += razao
  cont += 1
print("ACABOU")
