from services.whatsapp.filtro_mensagens import filtrar_atletas_para_envio
from services.whatsapp.mensagem import criar_mensagem
from services.whatsapp.whatsapp_service import enviar_whatsapp

def enviar_mensagens():

    atletas = filtrar_atletas_para_envio()

    for _, atleta in atletas.iterrows():

        telefone = atleta["Telefone envio"]
        nome = atleta["Nome"]

        mensagem = criar_mensagem(nome)

        enviar_whatsapp(telefone, mensagem)