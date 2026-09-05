
media = 100
desvio = 5
valor = 115

# Distância entre o valor e a média
distancia = valor - media

# Quantos desvios-padrão cabem nessa distância (Z-Score)
z_score = distancia / desvio

print(f"Média: {media}")
print(f"Desvio-padrão: {desvio}")
print(f"Valor: {valor}")
print(f"Distância até a média: {distancia}")
print(f"Z-Score: {z_score}")

# Interpretação em linguagem natural
if z_score == 0:
    interpretacao = "O valor está exatamente na média."
elif z_score > 0:
    interpretacao = (
        f"O valor está {abs(z_score)} desvios-padrão acima da média, "
        "ou seja, é maior que o normal esperado."
    )
else:
    interpretacao = (
        f"O valor está {abs(z_score)} desvios-padrão abaixo da média, "
        "ou seja, é menor que o normal esperado."
    )

print(f"Interpretação: {interpretacao}")
