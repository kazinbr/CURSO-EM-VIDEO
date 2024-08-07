'''
Desenvolva um programa que pergunte a distância
de uma viagem em KM. Calcule o preço da passagem, cobrando
R$0.50 por Km para viagens de até
200Km e R$0,45 para viagens mais longas
'''
km = int(input('Quantos Km será a sua viagem? '))
if km <= 200:
    print(f'Sua viagem custará R${0.50 * km:.0f},00!!')
else: 
    print(f'Sua viagem custará R${0.45 * km:.0f},00!!')