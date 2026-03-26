'''
Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso, de zero
até vinte.

Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
'''

cont =('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    per = int(input('Digite um número entre  0 a 20: '))
    if 0 <= per <= 20:
        print(f"O número que você digitou foi {cont[per]}.")
        
        continuar = input("Deseja continuar? [S/N] ")
        if continuar.upper() == "N":
            break
    else:
        print("Tente novamente! ", end="")