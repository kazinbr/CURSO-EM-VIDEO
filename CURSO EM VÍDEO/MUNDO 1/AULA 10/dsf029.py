'''
Escreva um programa que leia a velocidade de um carro

Se ele ultrapassar de 80km/h, mostre uma mensagem dizendo que 
ele foi multado!

A multa vai custar R$7,00 por cada KM acima do limite
'''
km = int(input('Quantos Km/h você estava dirigindo? '))
multa = (km - 80) * 7
if km > 80:
    print(f'Você foi multado!! Deverá pagar um valor de R${multa},00.')
print('Dirija com cuidado, e se beber, não dirija!')