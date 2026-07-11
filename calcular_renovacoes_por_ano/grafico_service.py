import matplotlib.pyplot as plt
from pathlib import Path

def gerar_grafico_renovacoes_por_ano(resultado_por_ano):

    pasta_temp = Path("temp")
    pasta_temp.mkdir(exist_ok=True)

    caminho_grafico = pasta_temp / "grafico_renovacoes.png"

    anos = [item["ano"] for item in resultado_por_ano]
    percentuais = [item["perc_renovaram"] for item in resultado_por_ano]

    plt.figure(figsize=(8,5))

    totais = [item["total"] for item in resultado_por_ano]

    barras = plt.bar(anos, percentuais)

    for barra, perc, total in zip(barras, percentuais, totais):
        plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height() + 1,
        f"{perc:.2f}%\n({total} atletas)",
        ha="center",
        va="bottom",
        fontsize=9
    )

    plt.tight_layout()

    plt.savefig(caminho_grafico)
    plt.close()

    return str(caminho_grafico)