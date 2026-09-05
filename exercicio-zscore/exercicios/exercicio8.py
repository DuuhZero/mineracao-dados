

import pandas as pd
import numpy as np

dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400],
}

df = pd.DataFrame(dados)

media = df["Requisicoes"].mean()
desvio = df["Requisicoes"].std()

print(f"Média de Requisicoes: {media:.2f}")
print(f"Desvio-padrão de Requisicoes: {desvio:.2f}\n")

df["Z_Score"] = (df["Requisicoes"] - media) / desvio
df["Status"] = np.where(df["Z_Score"].abs() > 3, "Investigar", "Comum")

print("DataFrame completo:")
print(df, "\n")

print("Linhas marcadas para investigação:")
print(df[df["Status"] == "Investigar"])
