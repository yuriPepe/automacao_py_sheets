import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

def ler_planilha(nome_planilha, nome_aba):

    # Conecta à conta Google
    gc = gspread.service_account(filename="credenciais.json")

    # Abre a planilha
    planilha = gc.open(nome_planilha)

    # Abre a aba
    aba = planilha.worksheet(nome_aba)

    # Cria o DataFrame
    df = pd.DataFrame(aba.get_all_records())

    # Retorna para quem chamou
    return df

