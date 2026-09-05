

casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z_score = (valor - media) / desvio

    if z_score > 0:
        posicao = "acima da média"
        significado = "o sinal positivo indica que o valor supera a média"
    elif z_score < 0:
        posicao = "abaixo da média"
        significado = "o sinal negativo indica que o valor é menor que a média"
    else:
        posicao = "exatamente na média"
        significado = "o valor zero indica que não há distância em relação à média"

    print(f"Valor: {valor} -> Z-Score: {z_score:.2f} -> Está {posicao}")
    print(f"  Explicação: {significado}.")

print(
    "\nResumo: Z positivo = valor acima da média; "
    "Z negativo = valor abaixo da média; "
    "Z igual a zero = valor igual à média."
)
