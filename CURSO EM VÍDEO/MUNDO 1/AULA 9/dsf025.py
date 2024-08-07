'''Crie um programa que leia o nome de uma pessoa
e diga se tem "Silva" no nome
'''
nome = input('Digite seu nome completo: ')
silva = nome.upper()
print(f'Seu nome tem "Silva" no meio? {'SILVA' in silva}\nQual o índice que se encontra seu nome? {silva.find('SILVA')}')
