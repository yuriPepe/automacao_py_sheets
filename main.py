from services.sheets_service import ler_planilha
from services.analise_service import calcular_renovacoes_por_ano, calcular_renovacoes_geral
from services.grafico_service import gerar_grafico_renovacoes_por_ano
from services.pdf_service import gerar_pdf
from ui.input_service import obter_aba, escolher_local_pdf

aba = obter_aba()

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