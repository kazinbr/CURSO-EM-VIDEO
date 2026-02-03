'''
Crie um programa que leia o nome e o preço de vários 
produto. O programa deverá perguntar se o usuário vai continuar.
No final, mostra:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato.
'''

tot = barato_val = caro = 0
barato = ' '


print("-=-"*10)
print('     LOJA DO ACRE     ')
print("-=-"*10)

while True:
    prod = str(input('Nome do Produto: '))
    val = float(input('Preço: R$'))
    tot += val
    if val >= 1000:
        caro += 1
    elif val < barato_val:
        barato = prod
        barato_val = val
    
    if barato_val == 0:
        barato_val = val
    
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
        if cont in ('S', 'N'):
            break
    if cont == 'N':
        break

print('-------- FIM DO PROGRAMA --------')
print(f'O total de compra foi R${tot:.2f}!\nTemos {caro} produtos custando mais de R$1000.00\nO produto mai barato foi {barato} que custa R${barato_val:.2f} ')