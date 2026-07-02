import gspread
from google.oauth2.service_account import Credentials

try:
    # Permissões
    SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly"
    "https://www.googleapis.com/auth/drive"
]

# Arquivo JSON baixado do Google Cloud
    credenciais = Credentials.from_service_account_file(
    "credenciais.json",
    scopes=SCOPES
)

# Conecta ao Google
    gc = gspread.authorize(credenciais)
    print("autenticou!")


except Exception as e:
    print(f"erro na autenticação: {e}")
