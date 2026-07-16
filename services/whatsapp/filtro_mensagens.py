from services.sheets_service import ler_planilha

def filtrar_atletas_para_envio():

    df = ler_planilha(
    "REMATRICULAS 2025 - 2026",
    "06.26"
    )

    atletas = df.copy()

    atletas["Renovou?"] = atletas["Renovou?"].astype(str).str.strip().str.upper()

    atletas = atletas[
    atletas["Renovou?"].isin(["NÃO", "NAO"])
]

    # Remove quem não possui telefone
    atletas = atletas[atletas["Telefone"].notna()]

    atletas = atletas[atletas["Telefone"] != ""]

    return atletas