print("Programa iniciado!")

import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

gc = gspread.service_account(filename="credenciais.json")

#abre planilha
planilha = gc.open_by_key('10gcHcFw1xIR4Uq0BBMblGHtk0b3mFqdvVMq7XtD7gs4')

#abre aba exata
aba = planilha.worksheet("07.26")

#lê os dados
df = pd.DataFrame(aba.get_all_records())

# Remove espaços extras da coluna Renovou
df["Renovou?"] = df["Renovou?"].astype(str).str.strip()

# Contagem
renovaram = (df["Renovou?"] == "Sim").sum()
nao_renovaram = (df["Renovou?"] == "Não").sum()

total = renovaram + nao_renovaram

porcentagem_renovaram = (renovaram / total) * 100
porcentagem_nao = (nao_renovaram / total) * 100

print("========== RELATÓRIO ==========")
print(f"Total de atletas: {total}")
print()
print(f"Renovaram: {renovaram}")
print(f"Não renovaram: {nao_renovaram}")
print()
print(f"Renovação: {porcentagem_renovaram:.2f}%")
print(f"Não renovação: {porcentagem_nao:.2f}%")
print("===============================")