import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

def ler_planilha(nome_planilha, aba):

    # Conecta à conta Google
    gc = gspread.service_account(filename="credenciais.json")

    # Abre a planilha
    sh = gc.open(nome_planilha)

    #Abre aba escolhida
    worksheet = sh.worksheet(aba)

    # Cria o DataFrame
    df = worksheet.get_all_records()

    # Retorna para quem chamou
    return df

