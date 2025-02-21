'''
Melhore o desafio 061, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa encerra 
quando ele disser que quer mostrar 0 termos
'''
termo = int(input('Escolha o termo da PA: '))
razao = int(input('Escolha a razão de sua PA: '))
resp = 10

while resp != 0:
  pa = termo
  mais = resp
  for i in range(mais):
    print(pa, end=" > ")
    pa += razao
  print("ACABOU")

  resp = int(input('Gostaria de ver mais quantos termos? '))
  
