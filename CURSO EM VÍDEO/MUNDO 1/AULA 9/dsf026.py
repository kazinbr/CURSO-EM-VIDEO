'''
Faça um programa que leia uma frase pelo teclado
e mostre:

- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
'''
frase = input('Digite um frase: ').strip()
print(f'Quantas vezes a letra "A" aparece? {frase.upper().count('A')}\nQual é o inice da primeira vez que a letra "A" aparece? {frase.upper().find('A') + 1}\nQual é o índice da última vez que a letra "A" aparece? {frase.upper().rfind('A') + 1}')
