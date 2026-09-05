

media_a = 100
desvio_a = 2

media_b = 100
desvio_b = 20

valor = 110

z_a = (valor - media_a) / desvio_a
z_b = (valor - media_b) / desvio_b

print(f"Grupo A -> média: {media_a}, desvio: {desvio_a}, valor: {valor}")
print(f"Z-Score no Grupo A: {z_a:.2f}")

print(f"\nGrupo B -> média: {media_b}, desvio: {desvio_b}, valor: {valor}")
print(f"Z-Score no Grupo B: {z_b:.2f}")

print("\nComparação:")
print(f"  Mesma distância absoluta: {valor - media_a} unidades em ambos os grupos.")
print(f"  Z-Score no Grupo A: {z_a:.2f} (muito alto)")
print(f"  Z-Score no Grupo B: {z_b:.2f} (baixo)")

print(
    "\nExplicação: o Z-Score não depende apenas da distância absoluta até a "
    "média, mas de quantos desvios-padrão essa distância representa. "
    "No Grupo A, o desvio-padrão é pequeno (2), então uma distância de 10 "
    "unidades corresponde a muitos desvios-padrão, tornando o valor bastante "
    "incomum. No Grupo B, o desvio-padrão é grande (20), então a mesma "
    "distância de 10 unidades é pequena em termos relativos, sendo um valor "
    "comum dentro da variabilidade natural do grupo."
)
