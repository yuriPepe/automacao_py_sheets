import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

#abre planilha
def _abrir_planilha(nome_planilha):
    gc = gspread.service_account(filename="credenciais.json")

    return gc.open(nome_planilha)

#retorna dados da aba planilha
def ler_planilha(nome_planilha, aba):
    planilha = _abrir_planilha(nome_planilha)
    worksheet = planilha.worksheet(aba)

    return pd.DataFrame(worksheet.get_all_records())

#lista todas abas da planilha
def listar_abas(nome_planilha):
    planilha = _abrir_planilha(nome_planilha)

    return [aba.title for aba in planilha.worksheets()]