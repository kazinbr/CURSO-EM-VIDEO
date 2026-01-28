'''
Crie um programa que leia a idade e o 
sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá peruntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos.
'''

h = m = i = 0

p = ""
cont = ''
print('-'*30)
print('   CADASTRE UMA PESSOA   ')
print('-'*30)

Id = 0

while True: 
    while True:
        Id = int(input('Idade: '))
        if Id >= 18:
            i =+1
        break
    while True:
        p = str(input('Sexo: [M/F]')).strip().upper()
        if p in ("M", "F"):
            if p == "M":
                h+=1
            elif p == "F":
                if Id >=20:
                    m+=1  
            break
    cont = str(input('Quer continuar? [S/N]')).strip().upper()
    if cont in ('S', 'N'):
        if cont == 'N':
            break

print(f'===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {i}\nTotal de homens registrados: {h}\nTotal de mulheres acima de 20 anos: {m}')