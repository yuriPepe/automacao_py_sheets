from services.whatsapp.filtro_mensagens import filtrar_atletas_para_envio

def teste_rows():

    atletas = filtrar_atletas_para_envio()

    for _, atleta in atletas.iterrows():
        telefone = atleta["Telefone"]
        nome = atleta["Usuário"]
        print(nome, telefone)

teste_rows()
