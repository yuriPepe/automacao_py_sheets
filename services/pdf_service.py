from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import Image
from reportlab.lib.styles import getSampleStyleSheet

def gerar_pdf(resultado, caminho_pdf):

    total = resultado["total"]
    renovaram = resultado["renovaram"]
    nao_renovaram = resultado["nao"]
    perc_renovaram = resultado["perc_renovaram"]
    perc_nao = resultado["perc_nao"]

    conteudo = []

    logo = Image("imagens/logo_jusc.png")

    # Define apenas a largura
    largura = 200

    # Calcula a altura proporcional
    altura = logo.imageHeight * largura / logo.imageWidth

    logo.drawWidth = largura
    logo.drawHeight = altura

    conteudo.append(logo)

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(
    caminho_pdf,
    topMargin=10,
    bottomMargin=20,
    leftMargin=40,
    rightMargin=40
)

    conteudo.append(
    Paragraph("<b>RELATÓRIO DE RENOVAÇÕES</b>", styles["Title"])
)

    conteudo.append(Spacer(1,20))

    conteudo.append(
    Paragraph(f"Total de atletas: <b>{total}</b>", styles["Normal"])
)

    conteudo.append(
    Paragraph(f"Renovaram: <b>{renovaram}</b>", styles["Normal"])
)

    conteudo.append(
    Paragraph(f"Não renovaram: <b>{nao_renovaram}</b>", styles["Normal"])
)

    conteudo.append(
    Paragraph(
        f"Taxa de renovação: <b>{perc_renovaram:.2f}%</b>",
        styles["Normal"]
    )
)

    conteudo.append(
    Paragraph(
        f"Taxa de não renovação: <b>{perc_nao:.2f}%</b>",
        styles["Normal"]
    )
)

    conteudo.append(Spacer(1,20))

    imagem = Image(
    "graficos/renovacoes.png",
    width=300,
    height=300
)

    conteudo.append(imagem)

    pdf.build(conteudo)
    

print("PDF criado com sucesso!")