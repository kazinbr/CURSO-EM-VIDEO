'''
Faça um programa que calcule a soma entre todos os números 
ímpares que são múltiplos de três e que se encontram
no intervalo de 1 até 500
'''
for i in range(0, 501):
    d = i % 3
    if d == 0:
        print(i)
