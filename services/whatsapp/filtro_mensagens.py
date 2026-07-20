from services.sheets_service import ler_planilha
import re

def normalizar_telefone(telefone):

    if telefone is None:
        return ""

    telefone = re.sub(r"\D", "", str(telefone))

    # Adiciona o código do Brasil se não existir
    if telefone and not telefone.startswith("55"):
        telefone = "55" + telefone

    return telefone

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

    atletas["Telefone envio"] = (
    atletas["Celular"]
    .fillna("")
    .astype(str)
    .str.strip()
)

    sem_celular = atletas["Telefone envio"] == ""

    atletas.loc[sem_celular, "Telefone envio"] = (
    atletas.loc[sem_celular, "Telefone"]
    .fillna("")
    .astype(str)
    .str.strip()
)

    # Remove quem continua sem telefone
    atletas = atletas[atletas["Telefone envio"] != ""]

    atletas["Telefone envio"] = atletas["Telefone envio"].apply(normalizar_telefone)

    return atletas