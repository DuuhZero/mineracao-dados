

import pandas as pd

dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40],
}

df = pd.DataFrame(dados)

media = df["Tentativas_Login"].mean()
desvio = df["Tentativas_Login"].std()

print(f"Média de tentativas de login: {media:.2f}")
print(f"Desvio-padrão: {desvio:.2f}\n")

df["Z_Score"] = (df["Tentativas_Login"] - media) / desvio

print("DataFrame completo:")
print(df, "\n")

eventos_investigar = df[df["Z_Score"].abs() > 3]

print("Eventos com |Z| > 3 (candidatos a investigação):")
print(eventos_investigar, "\n")

print(
    "Mensagem final: em segurança, um evento estatisticamente incomum, "
    "como um número de tentativas de login muito acima do padrão, pode "
    "ser justamente o dado mais importante da análise, pois pode indicar "
    "uma tentativa de ataque, uso indevido de credenciais ou uma falha no "
    "sistema. Por isso, outliers não devem ser descartados sem investigação: "
    "eles frequentemente carregam a informação mais relevante."
)
