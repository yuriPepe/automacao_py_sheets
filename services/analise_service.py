def calcular_renovacoes(df):
    # Remove espaços extras da coluna Renovou
    df["Renovou?"] = (df["Renovou?"].astype(str).str.strip().str.lower())


    # Contagem
    renovaram = (df["Renovou?"] == "sim").sum()
    nao_renovaram = (
        (df["Renovou?"] == "não").sum() | (df["Renovou?"] == "nao").sum()
)

    total = renovaram + nao_renovaram

    return {
        "total": total,
        "renovaram": renovaram,
        "nao": nao_renovaram,
        "perc_renovaram": renovaram/total*100,
        "perc_nao": nao_renovaram/total*100
    }