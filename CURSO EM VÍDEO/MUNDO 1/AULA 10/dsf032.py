'''
Faça um programa que leia um ano qualquer e mostre se ele é Bissexto
'''
ano = int(input('Digite qualquer ano: '))
if ano % 4 == 0:
    ano1 = ano % 100
    if ano1 != 0:
        print (f'O ano de {ano} é Bissexto!')
    else:
        print (f'O ano de {ano} não é Bissexto!!')
else:
    ano2 = ano % 400
    if ano2 == 0:
        print(f'O ano de {ano} é Bissexto!!')
    else:
        print (f'O ano de {ano} não é Bissexto!!')
