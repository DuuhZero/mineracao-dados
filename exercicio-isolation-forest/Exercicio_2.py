
import numpy as np
from sklearn.ensemble import IsolationForest

# Dados: pelo menos 12 medições de latência em milissegundos.
# Maioria entre 20 e 70 ms, com pelo menos dois valores acima de 200 ms.
latencia = [
    [32], [45], [28], [55],
    [40], [60], [35], [50],
    [65], [30], [48], [58],
    [250], [320]
]

latencia = np.array(latencia)

# Aplicando o Isolation Forest
modelo = IsolationForest(contamination=0.15, random_state=42)
modelo.fit(latencia)

rotulos = modelo.predict(latencia)

print("Classificação de cada medição de latência (ms):")
for valor, rotulo in zip(latencia.flatten(), rotulos):
    situacao = "ANOMALIA (candidato)" if rotulo == -1 else "normal"
    print(f"  Latência = {valor:4d} ms -> {situacao}")

candidatos = latencia[rotulos == -1].flatten()
print("\nCandidatos identificados:", candidatos)

print("""
Explicação dos candidatos identificados:
Os valores 250 ms e 320 ms destoam fortemente do restante das medições,
que ficam concentradas entre 20 e 70 ms. Por isso, o Isolation Forest os
isola com poucas divisões (partições) na árvore, sinalizando-os como
anomalias.

Uma latência alta sempre representa uma falha?

Não necessariamente. Uma latência alta pode ser causada por:
  - Congestionamento momentâneo da rede (muitos usuários ao mesmo tempo);
  - Instabilidade temporária do provedor de internet;
  - Um pico isolado de uso de banda (ex.: um grande download em andamento).
Uma falha real (queda de conexão, problema no roteador, etc.) é apenas uma
das possíveis explicações; é preciso investigar o contexto para confirmar.
""")
