from dotenv import load_dotenv
import os

load_dotenv()

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

if not WHATSAPP_TOKEN:
    raise RuntimeError("WHATSAPP_TOKEN não encontrado no arquivo .env")

if not PHONE_NUMBER_ID:
    raise RuntimeError("PHONE_NUMBER_ID não encontrado no arquivo .env")