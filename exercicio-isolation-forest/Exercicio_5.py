
import numpy as np
from sklearn.ensemble import IsolationForest

# Dados: consumo diário de água (litros)
consumo_agua = [
    [48], [52], [50], [55],
    [49], [53], [51], [54],
    [56], [12], [180],
]

consumo_agua = np.array(consumo_agua)
valores = consumo_agua.flatten()

# ----------------------------------------------------------------------
# 1) Regra fixa: sinalizar consumo muito baixo (< 30) ou muito alto (> 100)
# ----------------------------------------------------------------------
LIMITE_INFERIOR = 30
LIMITE_SUPERIOR = 100

candidatos_regra = (valores < LIMITE_INFERIOR) | (valores > LIMITE_SUPERIOR)

print("=== Regra fixa ===")
print(f"Limite inferior: {LIMITE_INFERIOR} L | Limite superior: {LIMITE_SUPERIOR} L")
for valor, sinalizado in zip(valores, candidatos_regra):
    situacao = "ANOMALIA (candidato)" if sinalizado else "normal"
    print(f"  Consumo = {valor:4d} L -> {situacao}")

# ----------------------------------------------------------------------
# 2) Isolation Forest
# ----------------------------------------------------------------------
modelo = IsolationForest(contamination=0.18, random_state=42)
rotulos = modelo.fit_predict(consumo_agua)
candidatos_if = rotulos == -1

print("\n=== Isolation Forest ===")
for valor, rotulo in zip(valores, rotulos):
    situacao = "ANOMALIA (candidato)" if rotulo == -1 else "normal"
    print(f"  Consumo = {valor:4d} L -> {situacao}")

# ----------------------------------------------------------------------
# 3) Comparação
# ----------------------------------------------------------------------
print("\n=== Comparação entre os métodos ===")
iguais = np.array_equal(candidatos_regra, candidatos_if)
print("Os candidatos encontrados pelos dois métodos são iguais?", "Sim" if iguais else "Não")

print("\nCandidatos pela regra fixa:      ", valores[candidatos_regra])
print("Candidatos pelo Isolation Forest:", valores[candidatos_if])

print("""
Explicação das limitações de uma regra fixa:
  - Exige que alguém defina manualmente os limites (30 e 100, neste caso),
    o que depende de conhecimento prévio do problema e pode ser arbitrário.
  - Não se adapta automaticamente se o padrão de consumo mudar ao longo
    do tempo (por exemplo, uma casa que passa a ter mais moradores).
  - Não considera a distribuição real dos dados: um limite "redondo" como
    100 pode não corresponder ao que realmente é incomum estatisticamente.
  - Funciona bem apenas para casos simples com uma única característica;
    não se generaliza facilmente para múltiplas variáveis combinadas.

Por que o Isolation Forest pode ser útil quando não existe um limite
definido previamente:
  - Ele aprende o padrão "normal" diretamente dos dados, sem necessidade
    de definir limites manualmente.
  - Consegue lidar com múltiplas características ao mesmo tempo,
    identificando combinações incomuns que uma regra simples não
    perceberia.
  - Se adapta a diferentes contextos e distribuições de dados sem
    reconfiguração manual dos limites.

Pergunta para discussão - É melhor definir manualmente um limite ou deixar
o modelo aprender o padrão dos dados?
Depende do contexto: quando existe um limite técnico ou regulatório claro
(ex.: um valor de segurança conhecido), uma regra fixa pode ser mais
transparente e fácil de explicar. Quando o padrão "normal" é complexo,
muda com o tempo, ou envolve várias variáveis, um modelo como o Isolation
Forest tende a ser mais robusto e flexível.
""")
