
nome = input('Digite seu nome: ')
if nome.isdigit():
    print('Voce nao digitou um texto valido')
    exit() 
elif nome.isspace():
    print('Voce nao digitou um texto valido')
    exit()
elif len(nome) <= 3:
    print('Voce nao digitou um texto valido')
    exit()
try:
    salario = float(input('Digite o seu salário: '))
except ValueError:
    print('Valor digitado incorreto')
    exit()

if salario < 1:
    print('Salario incorreto')
    exit()
    
try:
    valor_bonus = float(input('Digite o valor do bônus: '))
except ValueError:
    print('Valor digitado incorreto')
    exit()

if valor_bonus == 0 :
    print('valor bonus incorreto')
    exit()
    
kpi = 1000 + salario * valor_bonus
print(f'Olá {nome}, o seu valor bônus foi de {kpi}')