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

def analise_motivos(df):
    
    df["Por que não renovou?"] = df["Por que não renovou?"].apply(normalizar_texto)

    return df["Por que não renovou?"].value_counts()