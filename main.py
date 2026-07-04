from services.sheets_service import ler_planilha
from services.analise_service import calcular_renovacoes
from services.grafico_service import gerar_grafico
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

resultado = calcular_renovacoes(df)

gerar_grafico(resultado)

gerar_pdf(resultado, caminho_pdf)
