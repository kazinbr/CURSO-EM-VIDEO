'''
faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
correto.
'''
n = ''
while n != 'M' and n != 'F':
  n = str(input('Qual o seu sexo? [M/F] ')).strip().upper()
  if n != 'M' or 'F':
    print('Valores inválidos. Tente novamente.')
print(f'Sexo {n} foi registrado com sucesso!')