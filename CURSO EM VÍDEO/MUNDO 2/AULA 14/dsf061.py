'''
Refaça o desaio 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando uma estrutura while
'''
termo = int(input('Escolha o termo da PA: '))
razao = int(input('Escolha a razão de sua PA: '))
resp = "S"

while resp == 'S':
  pa = termo
  for i in range(10):
    print(pa, end=" > ")
    pa += razao
  print("ACABOU")
  resp = str(input('Gostaria de tentar outros números? [S/N] ')).strip().upper()

  if resp == 'S':
    termo = int(input('Escolha o termo da PA: '))
    razao = int(input('Escolha a razão de sua PA: '))