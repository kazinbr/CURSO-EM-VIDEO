''' 
Refaça o desafio 35, acrescentando o recurso de
mostrar que tipo de trânguilo será formado:

-Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes.
'''
r1 = int(input('Qual o comprimento da primeira reta? '))
r2 = int(input('Qual o comprimento da segunda reta? '))
r3 = int(input('Qual o comprimento da terceira reta? '))

if r1 + r2 > r3:
    if r3 + r2 > r1:
        if r3 + r1 > r2:
            print('Sim, é possível fazer um triângulo com estas três retas!!')
        if r1 == r2 == r3:
            print('E o possível triângulo será Equilátero!!')
        elif r1 == r2 or r1 == r3 or r2 == r3:
            print('E o possível triângulo será um Isóceles!!') 
        elif r1 != r2 and r3 and r2 != r1 and r3:
            print('E o possível triângulo será um Escaleno!!')
else:
    print('Infelizmente não é possível fazer um triângulo com estas três retas :(')
