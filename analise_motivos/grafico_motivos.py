import matplotlib.pyplot as plt

def gerar_grafico_motivos(resultado):

    motivos = [item["motivo"] for item in resultado]
    quantidades = [item["quantidade"] for item in resultado]
    percentuais = [item["percentual"] for item in resultado]

    plt.figure(figsize=(10, 6))

    barras = plt.barh(motivos, quantidades)

    plt.title("Motivos da não renovação")
    plt.xlabel("Quantidade de atletas")

    # Escreve quantidade e porcentagem ao lado de cada barra
    for barra, qtd, perc in zip(barras, quantidades, percentuais):
        plt.text(
            barra.get_width() + 0.2,
            barra.get_y() + barra.get_height()/2,
            f"{qtd} ({perc:.2f}%)",
            va="center"
        )

    plt.tight_layout()
    plt.show()
    plt.close()