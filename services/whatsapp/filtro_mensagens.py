import pandas as pd
from services.sheets_service import ler_planilha

def filtrar_atletas_para_envio():

    df = ler_planilha(
    "REMATRICULAS 2025 - 2026",
    06.26
    )

    atletas = df.copy()

    # Apenas quem não renovou
    atletas = atletas[atletas["Renovou?"] == "Não"]

    # Remove quem não possui telefone
    atletas = atletas[atletas["Telefone"].notna()]

    atletas = atletas[atletas["Telefone"] != ""]

    return atletas