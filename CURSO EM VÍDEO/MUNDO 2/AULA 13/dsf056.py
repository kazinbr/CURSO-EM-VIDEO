'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
'''
somaId = 0
maiorId = 0
nomVelho = ''
mulher = 0

for i in range(1, 5):
    print(f'----- {i} PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().lower())
    
    somaId += idade

    if sexo == 'm' and idade > maiorId:
        maiorId = idade
        nomVelho = nome
    if sexo == 'f' and idade < 20:
        mulher += 1
med = somaId / 4

print(f'A média de idade do grupo é {med:.1f} anos.')
if nomVelho:
    print(f'O homem mais velho é {nomVelho} com {maiorId} anos!')
else:
    print('Não há homens no grupo!')
print(f'Ao todo, há {mulher} mulheres com menos de 20 anos!')