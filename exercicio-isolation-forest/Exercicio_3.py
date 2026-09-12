
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Dados: [distância (km), litros consumidos]
consumo = [
    [10, 1.0], [20, 1.8], [30, 2.6], [40, 3.5], [50, 4.3], [60, 5.1],
    [70, 6.0], [80, 7.0], [90, 8.0],
    [100, 20.0],
]

consumo = np.array(consumo)

# Aplicando o Isolation Forest às duas características
modelo = IsolationForest(contamination=0.1, random_state=42)
rotulos = modelo.fit_predict(consumo)

print("Classificação de cada registro (distância, litros):")
for (dist, litros), rotulo in zip(consumo, rotulos):
    situacao = "ANOMALIA (candidato)" if rotulo == -1 else "normal"
    print(f"  Distância = {dist:5.1f} km | Litros = {litros:5.1f} -> {situacao}")

candidatos = consumo[rotulos == -1]
print("\nCombinação(ões) incomum(ns) identificada(s):")
print(candidatos)

print("""
Explicação:
O registro [100 km, 20.0 L] é incomum porque, para os demais dados, o
consumo cresce de forma praticamente linear com a distância (em torno de
0,09 a 0,10 L/km). Nesse caso específico, o consumo por km sobe para
0,20 L/km, o dobro do padrão observado — ou seja, o carro teria gasto
muito mais combustível do que o esperado para aquela distância.

Por isso, distância e litros consumidos devem ser analisados juntos: olhar
apenas para "20 litros" isoladamente não pareceria estranho (é um valor
alto, mas não absurdo), e olhar apenas para "100 km" também não indicaria
problema. É a RELAÇÃO entre as duas variáveis que revela a anomalia --
um consumo de combustível muito acima do esperado para a distância
percorrida.
""")

# Gráfico de dispersão
plt.figure(figsize=(7, 5))
normais = consumo[rotulos == 1]
plt.scatter(normais[:, 0], normais[:, 1], color="steelblue", label="Normal", s=70)
plt.scatter(candidatos[:, 0], candidatos[:, 1], color="crimson", label="Candidato (anomalia)", s=100, marker="X")
plt.xlabel("Distância percorrida (km)")
plt.ylabel("Litros consumidos")
plt.title("Consumo de combustível - Isolation Forest")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_exercicio3.png", dpi=150)
print("\nGráfico salvo em 'grafico_exercicio3.png'")
plt.show()
