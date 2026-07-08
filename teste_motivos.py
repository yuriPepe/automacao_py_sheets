from services.sheets_service import ler_planilha
from automacao_py_sheets.analise_motivos.analise_motivo_service import analise_motivos

df = ler_planilha(
    "REMATRICULAS 2025 - 2026",
    "06.26"
)

resultado = analise_motivos(df)

print(resultado)