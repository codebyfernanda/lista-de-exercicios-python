'''
Idade em Dias
Leia um valor inteiro correspondente à idade de uma pessoa em 
dias e informe-a em anos, meses e dias. Obs.: apenas para facilitar 
o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
Nos casos de teste nunca haverá uma situação que permite 12 meses 
e alguns dias, como 360, 363 ou 364. Este é apenas um exercício 
com objetivo de testar raciocínio matemático simples.
'''

# ============================================================================
# --------------------------Algoritmo Idade em Dias---------------------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

# Entrada de dados (total de dias)
idade_em_dias = int(input())

# Cálculo de quantos anos "cabem" no total de dias
anos = idade_em_dias // 365 

# Cálculo do que sobrou (o resto), depois de tirar os anos
restante = idade_em_dias % 365

# Cáculo dos meses (quantos meses de 30 dias cabem no que sobrou)
meses = restante // 30 

# Cálculo dos dias finais 
dias = restante % 30 

# Exibição conforme solicitado 
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================

'''
EXTRA!!!
Novo Enunciado: Contador de Vida Real
Problema: Desenvolva um programa que receba a data de nascimento 
de uma pessoa (dia, mês e ano) e calcule o total exato de dias 
vividos até a data atual. Regras de Cálculo: Considere o calendário 
gregoriano (incluindo anos bissextos). A contagem deve ser baseada na 
diferença absoluta entre a data de nascimento e a data de hoje. Entrada:
Três valores inteiros separados por espaço ou em linhas diferentes:
Dia de nascimento. Mês de nascimento. Ano de nascimento.
Saída: Um único valor inteiro representando o total de dias, seguido
da mensagem "dias de vida".
'''

# ============================================================================
# -----------------------Quantos Dias De Vida Já Viveu------------------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

from datetime import date 

# Lendo as entradas 
print('Digite a sua data de nascimento: ')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

# Criando objetos de data 
dataNasc = date(ano, mes, dia)
dataHoje = date.today() # Aqui, serve pra puxar a data atual do sistema

# Calculando a diferença 
diferenca = dataHoje - dataNasc

# Mostrando a saída
print(f'\nVocê viveu exatamente {diferenca.days} dias de vida.') # Aqui, o .days extrai o numero inteiro de dias do objeto diferenca

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================

