''' 
Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou
o prazo
'''
nasc = int(input('Em que ano você nasceu?? '))

cal = 2024 - nasc

if cal < 18:
    print(f'Faltam {18 - cal} anos para você se alistar!!')
elif cal == 18:
    print('Já está na hora de se alistar!!')
else:
    print(f'Você deveria ter se alistado há {cal - 18} anos!!')
