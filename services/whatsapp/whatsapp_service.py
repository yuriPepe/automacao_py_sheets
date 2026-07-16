import requests
from services.whatsapp.config import WHATSAPP_TOKEN, PHONE_NUMBER_ID

def enviar_whatsapp(numero, mensagem):

    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {
            "body": mensagem
        }
    }

    resposta = requests.post(
        url,
        headers=headers,
        json=payload
    )

    return resposta

resposta = enviar_whatsapp("5548988651056", "Mensagem teste")
print(resposta.status_code)
print(resposta.json())