
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Dados: velocidade de 18 veículos (km/h), medidos em uma via de 60 km/h
velocidades = [
    [58], [62], [55], [60], [63], [59],
    [61], [57], [64], [60], [58], [62],
    [56], [59], [61], [63],
    [5],    # situação incomum 1: veículo praticamente parado (pane/trânsito)
    [140],  # situação incomum 2: excesso de velocidade grave
]

velocidades = np.array(velocidades)

# Aplicando o Isolation Forest
modelo = IsolationForest(contamination=0.11, random_state=42)
rotulos = modelo.fit_predict(velocidades)

print("Classificação de cada velocidade (km/h):")
for valor, rotulo in zip(velocidades.flatten(), rotulos):
    situacao = "ANOMALIA (candidato)" if rotulo == -1 else "normal"
    print(f"  Velocidade = {valor:4d} km/h -> {situacao}")

candidatos = velocidades[rotulos == -1].flatten()
print("\nCandidatos identificados:", candidatos)

print("""
Explicação de cada candidato:
  - 5 km/h: velocidade extremamente baixa para a via. Pode representar um
    EVENTO LEGÍTIMO (congestionamento momentâneo) ou um CASO PARA
    INVESTIGAÇÃO (veículo com pane mecânica parado na pista, o que é um
    risco de segurança e merece atenção).
  - 140 km/h: excesso de velocidade muito acima do limite de 60 km/h.
    Não parece erro de medição (o radar registrou um valor plausível para
    um veículo), portanto é um CASO PARA INVESTIGAÇÃO / FISCALIZAÇÃO —
    possível infração de trânsito grave.

Critérios usados para decidir que uma observação era incomum:
  A maioria das velocidades está concentrada entre 55 e 64 km/h, uma faixa
  estreita e coerente com o limite da via. Os valores 5 e 140 km/h ficam
  muito distantes dessa faixa central, exigindo poucas divisões da árvore
  de isolamento para serem separados dos demais -- por isso, recebem um
  score de anomalia mais alto (caminho médio mais curto na árvore).
""")

# Gráfico
plt.figure(figsize=(8, 4.5))
indices = np.arange(len(velocidades))
normais_mask = rotulos == 1
plt.scatter(indices[normais_mask], velocidades.flatten()[normais_mask],
            color="steelblue", label="Normal", s=70)
plt.scatter(indices[~normais_mask], velocidades.flatten()[~normais_mask],
            color="crimson", label="Candidato (anomalia)", s=110, marker="X")
plt.axhline(60, color="gray", linestyle="--", linewidth=1, label="Limite da via (60 km/h)")
plt.xlabel("Observação (veículo nº)")
plt.ylabel("Velocidade (km/h)")
plt.title("Velocidade de veículos - Isolation Forest")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_exercicio6.png", dpi=150)
print("Gráfico salvo em 'grafico_exercicio6.png'")
plt.show()
