import pandas as pd

def calcular_renovacoes_por_ano(df):

    # Remove espaços extras da coluna Renovou
    df["Renovou?"] = (df["Renovou?"].astype(str).str.strip().str.lower())

    df["Início da Liberação"] = pd.to_datetime(
        df["Início da Liberação"],
        dayfirst=True,
        errors="coerce"

    )

    df["Ano"] = df["Início da Liberação"].dt.year

    resultado = []

    for ano, grupo in df.groupby("Ano"):

        renovaram = (grupo["Renovou?"] == "sim").sum()
        nao_renovaram = grupo["Renovou?"].isin(["não", "nao"]).sum()

        total = renovaram + nao_renovaram

        resultado.append({
            "ano": int(ano),
            "total": total,
            "renovaram": renovaram,
            "nao_renovaram": nao_renovaram,
            "perc_renovaram": renovaram / total * 100 if total else 0,
            "perc_nao": nao_renovaram / total * 100 if total else 0
        })

    return resultado