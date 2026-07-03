import matplotlib.pyplot as plt

def gerar_grafico(resultado):
        plt.figure(figsize=(6,6))

        plt.pie(
        [resultado["renovaram"], resultado["nao"]],
        labels=["Renovaram","Não renovaram"],
        autopct="%1.1f%%"
    )

        plt.savefig("graficos/renovacoes.png")

        plt.close()