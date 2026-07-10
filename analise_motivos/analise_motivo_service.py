import pandas as pd

import unicodedata

def normalizar_texto(texto):
    if texto is None:
        return ""

    texto = str(texto).strip().lower()

    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )

    return texto

def categorizar_motivo(motivo):

    if "lesao" in motivo or "cirurgia" in motivo or "machuc" in motivo:
        return "Lesão"

    elif "mudou" in motivo or "mudanca" in motivo or "cidade" in motivo:
        return "Mudança"

    elif "finance" in motivo or "dinheiro" in motivo or "valor" in motivo:
        return "Financeiro"

    elif "horario" in motivo or "tempo" in motivo:
        return "Horário"

    elif "aguardando resposta" in motivo:
        return "Aguardando resposta"

    else:
        return "Outros"

def analise_motivos(df):
    
    df["Por que não renovou?"] = df["Por que não renovou?"].apply(normalizar_texto)

    df = df[df["Por que não renovou?"] != ""]

    df["Categoria"] = (df["Por que não renovou?"].apply(categorizar_motivo))

    contagem = df["Categoria"].value_counts()

    resultado = []

    total = contagem.sum()

    for motivo, quantidade in contagem.items():

        resultado.append({
        "motivo": motivo,
        "quantidade": quantidade,
        "percentual": quantidade / total * 100
    })

    return resultado
