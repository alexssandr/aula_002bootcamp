# #### Inteiros (`int`)
import math

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#numero_1 = int(input('Digite o primeiro numero: '))
#numero_2 = int(input('Digite o segundo numero: '))
#soma_numeros = numero_1 + numero_2
#print(soma_numeros)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#numero_divisao = int(input('Digite o numero a ser dividido: '))
#resto_divisao = numero_divisao % 5
#print(resto_divisao)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#numero_1 = int(input('Digite o primeiro numero: '))
#numero_2 = int(input('Digite o segundo numero: '))
#numero_multiplicacao = numero_1 * numero_2
#print(numero_multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero_1 = int(input('Digite o primeiro numero: '))
# numero_2 = int(input('Digite o segundo numero: '))
# divisao_inteira = numero_1 // numero_2
# print(divisao_inteira)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero_1 = int(input('Digite o primeiro numero: '))
# quadradro_numero = numero_1 ** 2
# print(quadradro_numero)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_1 = float(input('Digite o primeiro numero: '))
# numero_2 = float(input('Digite o segundo numero: '))
# soma_float = numero_1 + numero_2
# print(soma_float)


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_1 = float(input('Digite o primeiro numero: '))
# numero_2 = float(input('Digite o segundo numero: '))
# media_numeros = (numero_1 + numero_2) / 2
# print(media_numeros)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# numero_1 = int(input('Digite a base:'))
# numero_2 = int(input('Digite o expoente:'))
# print(math.pow(numero_1,numero_2))

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# celsius = int(input("Enter the Temperature in Celsius:\n"))
# fahrenheit_temperature = (1.8 * celsius) + 32
# print(fahrenheit_temperature)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input('Digite o raio: '))
# area_circulo = math.pi * raio **2
# print(f'{area_circulo:.2f}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = input('Digite o texto: ')
# print(texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# texto = input('Digite o texto: ')
# print(texto.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# texto = input('Digite uma frase: ')
# print(texto.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# texto = input('Digite uma data: ')
# data_lista = texto.split('/')
# print('Dia:',data_lista[0])
# print('Mes:',data_lista[1])
# print('Ano:',data_lista[2])

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# texto_1 = input('Digite o texto 1: ')
# texto_2 = input('Digite o texto 2: ')
# print(texto_1 + texto_2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# valor1 = bool(input('digite True ou False: '))
# valor2 = bool(input('digite True ou False: '))
# print(valor1 and valor2)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# numero_1 = int(input('Digite o primeiro numero: \n'))
# numero_2 = int(input('Digite o segundo numero: \n'))

# if numero_1 == numero_2:
#     print('numeros iguais')
# else:
#     print('numeros diferentes')

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = int(input("Enter the Temperature in Celsius:\n"))
#     fahrenheit_temperature = (1.8 * celsius) + 32
#     print(fahrenheit_temperature)
# except ValueError:
#     print('valor incorreto')

# 22: Verificador de Palíndromo
# entrada = input("Digite uma palavra ou frase:\n")
# if isinstance(entrada, str):
#     print('é um texto')
# else:
#     print('nao é um texto')
# 23: Calculadora Simples
try:
    num1 = float(input('Digite o primeiro numero:\n'))
    num2 = float(input('Digite o segundo numero:\n'))
    operador = input('Digite o operador (+ - * /):\n')
    
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '-':
        resultado = num1 / num2

    print(resultado)
except:
    print('erro no processamento')
    


# 24: Classificador de Números
# 25: Conversão de Tipo com Validação