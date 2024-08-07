'''
Desenvolva um programa que leia primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros termos dessa progressão
'''
termo = int(input('Escolha o termo da PA: '))
razao = int(input('Escolha a razão de sua PA: '))
print(termo)
for i in range(1, 10):
    pa = termo + (razao * i)
    print(pa)
