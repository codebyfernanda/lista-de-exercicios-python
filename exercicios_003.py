'''
Exercício: Gasto de Combustível
Joaozinho quer calcular a quantidade de litros de combustível gastos em uma 
viagem, utilizando um automóvel que faz 12 KM/L. Para isso, o programa deve
receber o tempo gasto na viagem (em horas) e a velocidade média durante a 
mesma (em km/h).

A partir desses dados, é possível obter a distância percorrida e, em seguida,
calcular quantos litros seriam necessários para concluir o trajeto.

Entrada
O arquivo de entrada contém dois números inteiros: O tempo gasto na viagem 
(em horas). A velocidade média durante a viagem (em km/h).

Saída
Imprima a quantidade de litros necessária para realizar a viagem, formatada 
com três casas decimais após o ponto.
'''

# ============================================================================
# ----------------------------Gasto de Combustível----------------------------
# ------------------------Escrito por: @codebyfernanda------------------------
# ============================================================================

# Colocar entrada 
tempo = int(input())
velocidade = float(input())

# Calcular a distância 
distancia = velocidade * tempo

# Calcular do consumo: distância / eficiência (12 KM/L)
litros = distancia / 12

# Mostrar saída (formatada em 3 casas decimais)
print(f'{litros:.3f}')

# ============================================================================
# ----------------------------------------------------------------------------
# ============================================================================