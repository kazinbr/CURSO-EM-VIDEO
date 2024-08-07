'''
Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento.

para salários superiores a R$1.250,00. calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%.
'''
sal = int(input('Qual é o seu salário? '))
sup = (sal * 0.1) + sal
inf = (sal * 0.15) + sal

if sal > 1250:
    print(f'Você terá um aumento de 10%\nSendo assim, seu salário será de R${sup:.0f},00')
else:
    print(f'Você receberá um aumento de 15%!!\nSeu novo salário será de R${inf:.0f},00')
