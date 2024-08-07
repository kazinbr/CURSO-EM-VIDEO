''' 
Crie um programa que leia duas notas de um aluno e calcule sua média
mostrando uma mensagem no final, de acordo com a média atingida.

- Média abaixo de 5.0: Reprovado

- Média entre 5.0 e 6.9:
Recuperação

- Média 7.0 ou superior:
Aprovado
'''
n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))

med = (n1 + n2) / 2

if med < 5.0:
    print(f'Você foi REPROVADO!\nSua média foi de {med:.1f} pontos, estude mais!!')
elif 6.9 > med > 5.0:
    print(f'Você está de RECUPERAÇÃO!\nSua média foi de {med:.1f} pontos, boa prova!!')
else:
    print(f'Você foi APROVADO!!\nSua média foi de {med:.1f} pontos, parabéns!!')
    