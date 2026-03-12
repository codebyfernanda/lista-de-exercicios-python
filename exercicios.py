'''
1. Faça um programa que lê o valor da cotação do dólar em um determinado dia e
em seguida lê uma quantia em dólares. Realize a conversão para reais.
'''
# ============================================================================
# ------------Algoritmo Conversão de Dólares (US$) para Reais (R$)------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

# Lendo a contação do dólar
cotacaoDol = float(input('Digite o valor da cotação do dóla hoje (ex: 5.21 - COLOQUE COM PONTO (.) OBRIGATORIAMENTE!): ')) 

# Lendo a quantia em dólares que o usuário tem
quantidadeDol = float(input('Digite a quantia em doláres (US$): '))

# Cálculo da conversão 
reais = quantidadeDol * cotacaoDol

# Exibindo o resultado (com duas casas decimais)
print(f'O valorde US$ {quantidadeDol:.2f} convertido para reais é: R${reais:.2f}')

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================

'''
2. Ler dois valores para as variáveis A e B e efetue a troca dos valores de forma
que a variável A passe a possuir o valor da variável B e a variável B passe a
possuir o valor da variável A. Apresente os valores trocados.
'''

# ============================================================================
# ---------------Algoritmo de Troca dos Valores de 2 Variáveis----------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

# 1. Lendo os valores
A = input('Digite o valor de A: ')
B = input('Digite o valor de B: ')

print(f"\nAntes da troca: A = {A} e B = {B}")

# 2. Realizando a troca
A, B = B, A

# 3. Exibindo os valores trocados
print(f"Depois da troca: A = {A} e B = {B}")

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================

'''
3. Leia um valor inteiro e apresente os resultados do quadrado, do cubo e da raiz
quadrada do valor lido.
'''

# ============================================================================
# ----------Algoritmo de Cálculos do Quadrado, Cubo e Raiz Quadrada-----------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

import math

# Lendo o valor inteiro
numero = int(input("Digite um valor inteiro: "))

# Realizando os cálculos
quadrado = numero ** 2
cubo = numero ** 3
raizQuadrada = math.sqrt(numero)

# Exibindo os resultados
print("-" * 33)
print(f"Número original: {numero}")
print(f"Elevado ao quadrado: {quadrado}")
print(f"Elevado ao cubo: {cubo}")
print(f"Raiz quadrada: {raizQuadrada:.2f}")
print("-" * 33)
print("Processado por @codebyfernanda")

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================

'''
4. Receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) idade dessa pessoa;
b) quantos anos ela terá em 2050.
'''

# ============================================================================
# ---------------Algoritmo de Cálculo da idade e idade em 2050----------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

from datetime import date

# Lendo as entradas
anoNasc = int(input('Digite o ano em que você nasceu (ex: 1998): '))
anoAtual = date.today().year # Pega o ano do sistema

# Cálculos
idade = anoAtual - anoNasc
idade_2050 = 2050 - anoNasc

# Fornecendo as saídas
print("\n" + "-"*33)
print(f"Resultados para quem nasceu em {anoNasc}:")
print(f"a) Idade atual: {idade} anos")
print(f"b) Idade em 2050: {idade_2050} anos")
print("="*33)
print("Produzido por @codebyfernanda")

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================

'''
5. Receba o salário base de um funcionário, calcule e mostre o salário a receber,
sabendo-se que o funcionário tem gratificação de 10% sobre o salário base e paga
imposto de 4% sobre salario total.
'''

# ============================================================================
# -------------Algoritmo de Cálculo do Salário de um Funcionário--------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

# Entrada
salBase = float(input('Digite o sálario base do funcionário (R$): '))

# 2. Processamento
gratificacao = salBase * 0.10 # 10% de gratificação
salarioGratif = salBase + gratificacao

imposto = salarioGratif * 0.04 # 4% de imposto sobre o total
salFinal = salarioGratif - imposto

# Saída 
print("-" * 33)
print(f"Salário Base:    R$ {salBase:>8.2f}") # O símbolo :>8.2f dentro de uma string é um formatador de exibição!!!
print(f"Gratificação:  + R$ {gratificacao:>8.2f}")
print(f"Imposto (4%):  - R$ {imposto:>8.2f}")
print("-" * 33)
print(f"SALÁRIO LÍQUIDO: R$ {salFinal:>8.2f}")
print("-" * 33)
print("Folha de pagamento criada por @codebyfernanda")