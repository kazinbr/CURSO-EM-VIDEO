'''
Desenvolva um programa que leia primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa progressão
'''
termo = int(input('Escolha o termo da PA: '))
razao = int(input('Escolha a razão de sua PA: '))
pa = termo + (10-1) * razao
for i in range(termo, pa+razao, razao):
    print(i, end=" > ")
print("ACABOU")