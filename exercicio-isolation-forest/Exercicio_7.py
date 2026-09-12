
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Lendo o arquivo com pandas
dados = pd.read_csv("sensores_ambientais.csv")

# Exibindo as primeiras linhas
print("Primeiras linhas do arquivo:")
print(dados.head())

# Selecionando temperatura e umidade como características
caracteristicas = dados[["temperatura", "umidade"]]

# Aplicando o Isolation Forest
modelo = IsolationForest(contamination=0.1, random_state=42)
dados["rotulo"] = modelo.fit_predict(caracteristicas)

# rotulo == -1 -> candidato a anomalia | rotulo == 1 -> normal
print("\nDataFrame com a coluna 'rotulo' adicionada:")
print(dados)

# Mostrando os identificadores das leituras candidatas
candidatos = dados[dados["rotulo"] == -1]
print("\nIdentificadores das leituras candidatas:")
print(candidatos["id_leitura"].tolist())
print("\nDetalhes das leituras candidatas:")
print(candidatos)

print("""
Explicação:
A maior parte das leituras fica em uma faixa "confortável" de temperatura
(por volta de 20-24°C) e umidade (47-61%). As leituras sinalizadas fogem
bastante desse padrão -- por exemplo, temperatura muito baixa combinada
com umidade muito alta, ou temperatura alta combinada com umidade baixa.
Essa combinação incomum entre as duas variáveis (e não cada uma
isoladamente) é o que faz o Isolation Forest isolar essas leituras com
poucas divisões na árvore, sinalizando-as como possíveis anomalias --
que podem indicar um sensor com defeito, uma porta/janela aberta no
ambiente, ou uma condição climática realmente atípica.
""")

# Gráfico de dispersão
plt.figure(figsize=(7, 5))
normais = dados[dados["rotulo"] == 1]
plt.scatter(normais["temperatura"], normais["umidade"], color="steelblue", label="Normal", s=70)
plt.scatter(candidatos["temperatura"], candidatos["umidade"], color="crimson",
            label="Candidato (anomalia)", s=110, marker="X")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Umidade (%)")
plt.title("Sensores ambientais - Isolation Forest")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_exercicio7.png", dpi=150)
print("Gráfico salvo em 'grafico_exercicio7.png'")
plt.show()

# Salvando o resultado (com a coluna 'rotulo') em um novo arquivo CSV
dados.to_csv("sensores_ambientais_resultado.csv", index=False)
print("Resultado salvo em 'sensores_ambientais_resultado.csv'")
