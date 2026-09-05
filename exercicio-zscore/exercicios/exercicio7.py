

def interpretar_z(z):
    if abs(z) > 3:
        return "Investigar"
    elif z < 0:
        return "Abaixo da média"
    elif z > 0:
        return "Acima da média"
    else:
        return "Na média"


valores_z = [-3.5, -1.2, 0, 0.8, 3.7]

for z in valores_z:
    resultado = interpretar_z(z)
    print(f"Z = {z} -> {resultado}")
