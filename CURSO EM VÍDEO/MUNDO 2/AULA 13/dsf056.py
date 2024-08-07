'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
'''
for i in range(1, 5):
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual a sua idade? '))
    sexo = input('Feminino ou Masculino? ')
med = 