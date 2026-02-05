'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (Número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: COnsidere que o caixa possui cédulas de R$50, R$20, R$10 e R$1/
'''

tot = cin = vin = dez = um = 0

print('==='*10)
print('          BANCO')
print('==='*10)

while True:
    val = int(input('Qual valor você quer sacar? R$ '))
    cin = int(val/50)
    tot = cin*50
    val = val - tot

    if val != 0:
        vin = int(val/20)
        tot = vin*20
        val = val - tot
        if val != 0:
            dez = int(val/10)
            tot = dez*10
            val = val - tot
            if val != 0:
                um = int(val/1)


    break
print(f'Total de {cin} cédulas de R$50\nTotal de {vin} cédulas de R$20\nTotal de {dez} cédula de R$10\nTotal de {um} cédulas de R$1')
print('==='*10)
print('Volte sempre ao Banco! Tenha um bom dia!')