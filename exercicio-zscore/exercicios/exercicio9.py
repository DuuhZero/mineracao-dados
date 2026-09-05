
import numpy as np

dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]

# Cálculo do IQR
q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}\n")

# Cálculo do Z-Score
media = np.mean(dados)
desvio = np.std(dados)

valor = 30
z_score = (valor - media) / desvio

print(f"Média: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}")
print(f"Z-Score de {valor}: {z_score:.2f}\n")

# Comparação
fora_do_iqr = valor > limite_superior or valor < limite_inferior
print(f"O valor {valor} está fora dos limites do IQR? {fora_do_iqr}")
print(f"O valor {valor} tem |Z| > 3? {abs(z_score) > 3}")

print(
    "\nConclusão: o IQR marca o valor 30 como um outlier claro, pois ele "
    "ultrapassa bastante o limite superior calculado a partir dos quartis. "
    "Já o Z-Score pode não ultrapassar o limiar de |Z| > 3, pois o próprio "
    "valor 30 infla a média e o desvio-padrão do conjunto (que é pequeno). "
    "Isso mostra que técnicas diferentes podem analisar o mesmo dado por "
    "critérios diferentes: o IQR é mais robusto a valores extremos, "
    "enquanto o Z-Score é sensível a eles, já que média e desvio-padrão "
    "usam todos os valores do conjunto, incluindo o próprio outlier."
)
