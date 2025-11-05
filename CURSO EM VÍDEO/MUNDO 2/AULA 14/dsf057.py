'''
faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
correto.
'''
n = str(input('Qual o seu sexo? [M/F] ')).strip().upper() [0]

while n != 'M' and n != 'F':
  n = str(input('Valores inválidos. Digite novamente [M/F]: ')).strip().upper() [0]
          
print(f'Sexo {n} foi registrado com sucesso!')