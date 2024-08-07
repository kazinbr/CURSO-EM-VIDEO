'''
Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
nome = input('Digite seu nome completo: ').strip()
print(f'Qual é o seu primeiro nome? {nome.split()[0]}\nQual é o seu último nome? {nome.split()[-1]}\nSeu nome tem "SILVA" no meio? {"SILVA" in nome.upper()}')
