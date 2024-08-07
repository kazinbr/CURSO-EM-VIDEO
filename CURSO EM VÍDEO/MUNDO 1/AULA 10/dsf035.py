'''
Deselvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não
formar um triângulo
'''
r1 = int(input('Qual o comprimento da primeira reta? '))
r2 = int(input('Qual o comprimento da segunda reta? '))
r3 = int(input('Qual o comprimento da terceira reta? '))

if r1 + r2 > r3:
    if r3 + r2 > r1:
        if r3 + r1 > r2:
            print('Sim, é possível fazer um triângulo com estas três retas!!')
else:
    print('Infelizmente não é possível fazer um triângulo com estas três retas :(')
