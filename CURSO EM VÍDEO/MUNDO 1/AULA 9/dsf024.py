''' Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO"
'''
cid = input('Digite o nome de sua cidade: ')
div = cid.upper().split()
print(f'A primeira palavra começa com "SANTO"? {'SANTO' in div[0]}')
