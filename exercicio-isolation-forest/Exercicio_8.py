

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Lendo o arquivo com pandas
dados = pd.read_csv("vendas_ecommerce.csv")

# Exibindo as primeiras linhas
print("Primeiras linhas do arquivo:")
print(dados.head())

# Selecionando as características do modelo
# (id_venda NÃO é utilizado como característica, pois é apenas um identificador)
caracteristicas = dados[["valor_total", "quantidade_itens", "desconto_percentual"]]

# Aplicando o Isolation Forest
# contamination=0.15 -> captura as 3 vendas mais destoantes do conjunto
modelo = IsolationForest(contamination=0.15, random_state=42)
dados["rotulo"] = modelo.fit_predict(caracteristicas)

print("\nDataFrame com a coluna 'rotulo' adicionada:")
print(dados)

# Mostrando as vendas candidatas
candidatas = dados[dados["rotulo"] == -1]
print("\nVendas candidatas (possíveis anomalias):")
print(candidatas)

print("""
Explicação de por que essas vendas foram sinalizadas:
A maioria das vendas tem valor_total entre ~R$70 e R$420, quantidade de
itens entre 1 e 8, e desconto entre 0% e 20% -- um padrão coerente entre
as três variáveis (mais itens/desconto tende a acompanhar um valor maior).
As vendas sinalizadas fogem desse padrão combinado, por exemplo:
  - Um valor_total muito alto associado a um desconto percentual também
    muito alto (fora da faixa usual de desconto), o que pode indicar uma
    PROMOÇÃO LEGÍTIMA muito agressiva, um ERRO DE REGISTRO (preço ou
    desconto digitado incorretamente), ou uma venda que merece
    INVESTIGAÇÃO (possível fraude ou erro de sistema).
  - Uma quantidade de itens muito fora do padrão (muito acima do normal,
    como 25 itens contra uma média de 1 a 8) combinada com um
    valor_total baixo, sugerindo um possível erro de preço unitário ou
    um pedido corporativo/atacado, que também merece verificação.

Avaliação: cada caso deve ser analisado individualmente -- olhando a data
da venda, se houve campanha de marketing ativa, e conferindo o cadastro
do produto -- para decidir se é erro, promoção legítima ou fraude/caso
para investigação.
""")

# Visualização: valor_total x desconto_percentual, com o tamanho do ponto
# representando a quantidade de itens
plt.figure(figsize=(8, 5.5))
normais = dados[dados["rotulo"] == 1]
plt.scatter(normais["valor_total"], normais["desconto_percentual"],
            s=normais["quantidade_itens"] * 12, color="steelblue",
            alpha=0.7, label="Normal")
plt.scatter(candidatas["valor_total"], candidatas["desconto_percentual"],
            s=candidatas["quantidade_itens"] * 12, color="crimson",
            alpha=0.9, label="Candidata (anomalia)", marker="X")
plt.xlabel("Valor total (R$)")
plt.ylabel("Desconto (%)")
plt.title("Vendas de e-commerce - Isolation Forest\n(tamanho do ponto = quantidade de itens)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_exercicio8.png", dpi=150)
print("Gráfico salvo em 'grafico_exercicio8.png'")
plt.show()

# Salvando o resultado (com a coluna 'rotulo') em um novo arquivo CSV
dados.to_csv("vendas_ecommerce_resultado.csv", index=False)
print("Resultado salvo em 'vendas_ecommerce_resultado.csv'")
