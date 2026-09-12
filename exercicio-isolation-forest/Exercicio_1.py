
import numpy as np
from sklearn.ensemble import IsolationForest

# Dados fornecidos: quantidade de produtos vendidos em cada dia
vendas = [
    [80], [85], [90], [88],
    [92], [87], [95], [89],
    [91], [400]
]

vendas = np.array(vendas)

# Criando o modelo Isolation Forest
# contamination=0.1 -> esperamos aproximadamente 1 candidato a cada 10 observações
modelo = IsolationForest(contamination=0.1, random_state=42)
modelo.fit(vendas)

# Classificação: 1 = normal, -1 = anomalia (candidato)
rotulos = modelo.predict(vendas)

print("Classificação de cada venda:")
for valor, rotulo in zip(vendas.flatten(), rotulos):
    situacao = "ANOMALIA (candidato)" if rotulo == -1 else "normal"
    print(f"  Venda = {valor:4d} -> {situacao}")

# Mostrando o(s) valor(es) sinalizado(s)
candidatos = vendas[rotulos == -1].flatten()
print("\nValor(es) sinalizado(s) pelo modelo:", candidatos)

# Explicação
print("""
Explicação:
Uma venda muito acima do padrão normal (400 unidades, enquanto o restante
fica entre 80 e 95) pode ter diferentes causas:
  - Promoção: um desconto ou campanha de marketing pode ter aumentado
    bastante as vendas naquele dia específico.
  - Encomenda: um cliente (ex.: outro comércio) pode ter feito uma compra
    grande de uma só vez, fugindo do padrão do consumidor comum.
  - Erro de registro: pode ter havido um erro de digitação ou duplicidade
    no sistema de vendas, inflando o número real.

O valor 400 deve ser removido automaticamente?

Não necessariamente. O Isolation Forest apenas sinaliza o dado como incomum
estatisticamente; a decisão de remover, corrigir ou investigar deve ser
tomada por uma pessoa, considerando o contexto do negócio (por exemplo,
verificando se houve promoção ou conferindo a nota fiscal daquele dia).
""")
