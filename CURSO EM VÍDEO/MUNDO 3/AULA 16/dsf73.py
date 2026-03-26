'''
Crie uma tupla preenchida com os 20
primeiros colocados da Tabela do Campeonato Brasileiro do Futebol,
na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.
b) os últimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela esta o time da chapecoense.
'''

times = ("Palmeiras", "São Paulo", 'Fluminense', 'Flamengo', 'Bahia', 'Athletico-PR', 'Coritiba', 'Grêmio', 'Vasco da Gama', 
         'EC Vitória','Corinthians', 'Internacional', 'Atlético-MG', 'Bragantino', 'Chapecoense', 'Santos', 'Botafogo', 'Mirassol', 'Remo', 'Cruzeiro')

print("-=-"*10)
print(f"Lista dos times do Brasileirão: {times}")
print("-=-"*10)
print(f'Os 5 primeiros colocados do Brasileirão são: {times[0:4]}')
print("-=-"*10)
print(f"Os últimos 4 colocados da lista são: {times[-4:]}")
print("-=-"*10)
print(f"Em ordem alfabética: {sorted(times)}")
print("-=-"*10)
print(f"A Chapecoense está na {times.index("Chapecoense")+1}ª posição")