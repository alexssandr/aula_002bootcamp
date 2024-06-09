nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    nome = input('Digite seu nome: ')
    if nome.isdigit():
        print('Voce nao digitou um texto valido')
    elif nome.isspace():
        print('Voce nao digitou um texto valido')
    elif len(nome) <= 3:
        print('Voce nao digitou um texto valido')
    else:
        nome_valido = True

while not salario_valido:
    try:
        salario = float(input('Digite o seu salário: '))
        if salario < 1:
            print('Salario incorreto')
        else:
            salario_valido = True
    except ValueError:
        print('Valor digitado incorreto')

while not bonus_valido:
    
    try:
        valor_bonus = float(input('Digite o valor do bônus: '))
        if valor_bonus == 0 :
            print('valor bonus incorreto')
        else:
            bonus_valido = True
    except ValueError:
        print('Valor digitado incorreto')

kpi = 1000 + salario * valor_bonus
print(f'Olá {nome}, o seu valor bônus foi de {kpi}')