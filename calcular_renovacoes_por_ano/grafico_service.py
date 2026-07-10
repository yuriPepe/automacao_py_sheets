import matplotlib.pyplot as plt
from pathlib import Path

def gerar_grafico_renovacoes_por_ano(resultado_por_ano):

    pasta_temp = Path("temp")
    pasta_temp.mkdir(exist_ok=True)

    caminho_grafico = pasta_temp / "grafico_renovacoes.png"

    anos = [item["ano"] for item in resultado_por_ano]
    percentuais = [item["perc_renovaram"] for item in resultado_por_ano]

    plt.figure(figsize=(8,5))

    plt.bar(anos, percentuais)


    plt.title("Percentual de Renovação por Ano de Entrada")
    plt.xlabel("Ano de Entrada")
    plt.ylabel("% de Renovação")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 5))

    for i, valor in enumerate(percentuais):
        plt.text(i, valor + 1, f"{valor:.1f}%", ha="center")

    plt.tight_layout()

    plt.savefig(caminho_grafico)
    plt.close()

    return str(caminho_grafico)