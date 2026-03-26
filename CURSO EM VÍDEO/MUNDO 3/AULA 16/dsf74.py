'''
Crie um programa que vai gerar cinco
números aleatórios e colocar em uma tupla. 
Deois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão
na tulpa
'''
import random
numero = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)

print("Os números gerados foram:", *numero)
print(f"O número mais alto é {max(numero)}")
print(f"O número mais baixo é {min(numero)}")