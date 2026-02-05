'''
Crie um programa que leia o nome e o preço de vários 
produto. O programa deverá perguntar se o usuário vai continuar.
No final, mostra:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato.
'''

tot = barato_val = caro  = cont = 0
barato = ''


print("-=-"*10)
print('{:^30}'.format('LOJA DO ACRE'))
print("-=-"*10)

while True:
    prod = str(input('Nome do Produto: '))
    val = float(input('Preço: R$'))
    cont += 1
    tot += val
    if val >= 1000:
        caro += 1
    if cont == 1 or val < barato_val:
        barato_val = val
        barato = prod
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de compra foi R${tot:.2f}!\nTemos {caro} produtos custando mais de R$1000.00\nO produto mai barato foi {barato} que custa R${barato_val:.2f} ')