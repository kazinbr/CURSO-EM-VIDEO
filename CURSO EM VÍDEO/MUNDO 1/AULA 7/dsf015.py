D = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
c = input("teve algum defeito? ")
v = (D*60) + (k*0.15)

if c == "sim":
    print(f'O total a pagar é de R${(v*0.30)+ v:.2f}')
if c == 'não':
    print(f'O total a pagar é de R${(D*60) + (k*0.15):.2f}')
