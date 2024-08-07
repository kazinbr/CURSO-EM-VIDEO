''' 
Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamento:

- A vista dinheiro/cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
valor = float(input('Qual será o valor a ser pago? '))
pag = input('Qual será sua forma de pagamento? ')
pg = pag.upper() 

    
if 'VISTA' in pg:
    print(f'Você recebeu 10% de desconto!!\nO valor a ser pago será R${valor - (valor * 0.1):.2f}!!')
elif 'CARTAO' in pg:
    print(f'Você recebeu 5% de desconto!!\nO valor a ser pago será R${valor - (valor * 0.05):.2f}!!')
elif 'PARCELADO' in pg:
    if '2' in pg:
        print(f'Você pagará o valor normal do produto\nQue será de R${valor:.2f}!!')
    else:
        print(f'Você terá que pagar 20% de juros!\nO valor a ser pago será de R${valor + (valor * 0.2):.2f}')
