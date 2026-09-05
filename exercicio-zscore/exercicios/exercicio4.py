
import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]

media = np.mean(latencias)
desvio = np.std(latencias)

valor_investigado = 180
z_score = (valor_investigado - media) / desvio

print(f"Latências: {latencias}")
print(f"Média: {media:.2f} ms")
print(f"Desvio-padrão: {desvio:.2f} ms")
print(f"Z-Score de {valor_investigado} ms: {z_score:.2f}")

if abs(z_score) > 3:
    print(f"O valor {valor_investigado} ms merece investigação (|Z| > 3).")
else:
    print(f"O valor {valor_investigado} ms não ultrapassa o limite de |Z| > 3.")

print(
    "\nLembrete: investigar não significa apagar automaticamente. "
    "Um Z-Score alto indica um ponto fora do padrão, mas a causa "
    "(erro de medição, evento real, etc.) deve ser analisada antes "
    "de qualquer decisão sobre o dado."
)
