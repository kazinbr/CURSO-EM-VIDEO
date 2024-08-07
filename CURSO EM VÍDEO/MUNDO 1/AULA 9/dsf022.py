'''Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas
 - O nome com todas minúsculas
 - Quantas letras ao todo(sem considerar espaços)
 - Quantas letras tem o primeiro nome
'''
nome = input('Qual é o seu nome? ')
print(nome.upper())
print(nome.lower())
print(len(''.join(nome.split())))
print(len(nome.split()[0]))
