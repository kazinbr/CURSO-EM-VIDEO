''' 
Escreva um programa para aprovar o empréstimo bancário para a compra 
de uma casa. O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário, ou então o empréstimo será negado
'''

casa = float(input('Qual será o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))

cal = casa / (anos * 12)
csal = sal * 0.3

if cal > csal:
    print(f'Seu crédito foi \033[31mreprovado!!\033[m\nNão poderemos te dar o empréstimo de R${casa}, pois as parcelas de {cal:.2f} excedem o valor\nde seu salário :(')
else:
    print(f'Seu crédito foi \033[32maprovado!!\033[m\nPoderemos te dar o empréstimo de R${casa}!\nSuas parcelas serão de R${cal:.2f}')
