'''
Faça um programa que concede uma promoção de 20% de desconto no lanche
se a pessoa tiver o nome "JUVENILDO" no segundo nome

se ela não tiver, ela terá q pagar o dobro do valor do lanche
'''

nome = input('Digite o seu nome: ')
lanche = int(input('Qual o valor a ser pago pelo lanche? '))
div = nome.upper().split()

if 'JUVENILDO' in div[1]:
    print(f'Você recebeu 20% de desconto!!\nO valor a ser pago será de R${lanche - (lanche * 0.2):.2f}')
else:
    print(f'Certo, você terá que pagar o dobro do valor de seu lanche!!\nO valor a ser pago será de R${lanche * 2:.2f}')
