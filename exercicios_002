'''
Exercício: O Maior
Faça um programa que leia três valores inteiros e apresente o maior dos três 
valores lidos seguido da mensagem "eh o maior".Para resolver este problema, 
utilize a fórmula que calcula o maior entre dois valores. Nota: A fórmula 
acima calcula apenas o maior entre os dois primeiros valores. Portanto, 
um segundo passo é necessário para comparar o resultado obtido com o 
terceiro valor ($c$) e chegar ao resultado final esperado. Entrada - 
O arquivo de entrada contém três valores inteiros. Saída - Imprima o
maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

# ============================================================================
# --------------------------Descubra o maior número---------------------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

import math

# Versão "clássicão"

'''
# Lendo os três valores na mesma linha
a = int(input("Digite o primeiro: "))
b = int(input("Digite o segundo: "))
c = int(input("Digite o terceiro: "))
'''

# OU no 'padrão do beecrowd" 
# Deve digitar assim no console: 7 14 106 [ENTER]

linha = input().split() 
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

# Descobrir o maior entre A e B
maiorAb = (a + b + abs(a - b)) // 2

# Descobrir o maior entre o resultado anterior e C
resultadoFinal = (maiorAb + c + abs(maiorAb - c)) // 2

print(f"{resultadoFinal} eh o maior")

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================