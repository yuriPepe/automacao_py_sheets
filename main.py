from services.sheets_service import ler_planilha
from calcular_renovacoes_por_ano.analise_service import calcular_renovacoes_por_ano, calcular_renovacoes_geral
from calcular_renovacoes_por_ano.grafico_service import gerar_grafico_renovacoes_por_ano
from calcular_renovacoes_por_ano.pdf_service import gerar_pdf
from ui.input_service import obter_aba, escolher_local_pdf, escolher_relatorio
from analise_motivos.analise_motivo_service import analise_motivos
from analise_motivos.grafico_motivos import gerar_grafico_motivos

def gerar_relatorio_renovacoes():

    aba = obter_aba()

    if not aba:
        print("operação cancelada")
        exit()

    caminho_pdf = escolher_local_pdf(f"Relatorio_Renovacoes_{aba}.pdf")

    if not caminho_pdf:
        print("Operação cancelada.")
        exit()

    df = ler_planilha(
    "REMATRICULAS 2025 - 2026",
    aba
    )   

    resultado_por_ano  = calcular_renovacoes_por_ano(df)

    resultado_geral = calcular_renovacoes_geral(df)

    caminho_grafico = gerar_grafico_renovacoes_por_ano(resultado_por_ano)

    gerar_pdf(resultado_por_ano, resultado_geral, caminho_pdf, caminho_grafico)

def gerar_relatorio_motivos():

    aba = obter_aba()

    if not aba:
        print("operação cancelada")
        exit()

    df = ler_planilha(
    "REMATRICULAS 2025 - 2026",
    aba
    )  

    resultado = analise_motivos(df)

    grafico_motivos = gerar_grafico_motivos(resultado)

tipo = escolher_relatorio()

if tipo == "renovacoes":
    gerar_relatorio_renovacoes()

elif tipo == "motivos":
    gerar_relatorio_motivos()
