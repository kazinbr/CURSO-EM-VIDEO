'''
Crie um programa que leia uma frase qualquer e diga se ela é
um palindromo, deesconsiderando os espaços

Ex: ovo
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''
pal = input("Digite um palíndromo: ")
trat = pal.lower().strip().replace(" ", "")
inv = "".join(reversed(trat))

if inv == trat:
    print(f"A palavra \033[0;36m{pal}\033[m ao contrário fica \033[0;33m{"".join(reversed(pal))}\033[m\nESSA PALAVRA É UM \033[0;32mPALÍNDROMO!\033[m")
else:
    print(f"A palavra \033[0;36m{pal}\033[m ao contrário fica \033[0;33m{"".join(reversed(pal))}\033[m\nESSA PALAVRA \033[1mNÃO\033[m É UM \033[0;31mPALÍNDROMO\033[m")