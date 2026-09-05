
temperaturas = [21, 23, 25, 27, 29]
media = 25
desvio = 2

z_scores = [(temp, (temp - media) / desvio) for temp in temperaturas]

for temp, z in z_scores:
    print(f"Temperatura: {temp} -> Z-Score: {z:.2f}")

# Encontrando o valor com maior |Z|
mais_incomum = max(z_scores, key=lambda item: abs(item[1]))

print(
    f"\nA leitura mais incomum é {mais_incomum[0]}°C, "
    f"com Z-Score de {mais_incomum[1]:.2f} "
    f"(|Z| = {abs(mais_incomum[1]):.2f})."
)
