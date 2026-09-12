
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Dados: [passageiros, atraso em minutos]
viagens = [
    [32, 3], [45, 5], [50, 4],
    [60, 6], [55, 5], [70, 7],
    [65, 6], [80, 8], [75, 7],
    [10, 45],
]

viagens = np.array(viagens)

# Aplicando o Isolation Forest às duas características
modelo = IsolationForest(contamination=0.1, random_state=42)
rotulos = modelo.fit_predict(viagens)

print("Classificação de cada viagem (passageiros, atraso em min):")
for (passageiros, atraso), rotulo in zip(viagens, rotulos):
    situacao = "ANOMALIA (candidato)" if rotulo == -1 else "normal"
    print(f"  Passageiros = {passageiros:3d} | Atraso = {atraso:3d} min -> {situacao}")

candidatos = viagens[rotulos == -1]
print("\nViagem(ns) candidata(s):")
print(candidatos)

print("""
Explicação:
Nas demais viagens, quanto mais passageiros, maior tende a ser o atraso
(mais paradas para embarque/desembarque), mas sempre numa faixa moderada
(entre 3 e 8 minutos). A viagem [10 passageiros, 45 minutos] rompe esse
padrão: poucos passageiros, mas um atraso enorme. Isso é incomum porque,
com poucos passageiros, o esperado seria um atraso pequeno -- a
combinação das duas variáveis é o que evidencia o problema, não cada
variável isoladamente.

Possíveis causas para essa viagem:
  - Congestionamento intenso no trajeto;
  - Acidente de trânsito no percurso;
  - Falha mecânica do veículo (pane, pneu furado, etc.);
  - Desvio de rota por obras ou interdição da via.
""")

# Gráfico de dispersão
plt.figure(figsize=(7, 5))
normais = viagens[rotulos == 1]
plt.scatter(normais[:, 0], normais[:, 1], color="steelblue", label="Normal", s=70)
plt.scatter(candidatos[:, 0], candidatos[:, 1], color="crimson", label="Candidato (anomalia)", s=100, marker="X")
plt.xlabel("Número de passageiros")
plt.ylabel("Atraso (minutos)")
plt.title("Viagens de ônibus urbano - Isolation Forest")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_exercicio4.png", dpi=150)
print("Gráfico salvo em 'grafico_exercicio4.png'")
plt.show()
