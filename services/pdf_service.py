from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import Image
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os

def gerar_pdf(resultado_por_ano, resultado_geral, caminho_pdf, caminho_grafico):

    for item in resultado_por_ano:
        ano = item["ano"]
        total = item["total"]
        renovaram = item["renovaram"]
        nao_renovaram = item["nao_renovaram"]
        perc_renovaram = item["perc_renovaram"]
        perc_nao = item["perc_nao"]


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
    
    conteudo.append(Spacer(1,30))
    

    dados = [
    ["Ano", "Atletas", "Renovaram", "Não Renovaram"]
]
    
    total_atletas = 0

    for item in resultado_por_ano:

        total_atletas += item["total"]

        dados.append([
            item["ano"],
            item["total"],
            f'{item["renovaram"]} ({item["perc_renovaram"]:.1f}%)',
            f'{item["nao_renovaram"]} ({item["perc_nao"]:.1f}%)'
    ])
        

    

    dados.append([
        "TOTAL",
        resultado_geral["total"],
        f'{resultado_geral["renovaram"]} ({resultado_geral["perc_renovaram"]:.1f}%)',
        f'{resultado_geral["nao_renovaram"]} ({resultado_geral["perc_nao"]:.1f}%)'
])

    tabela = Table(dados)

    tabela.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),

    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0,0), (-1,0), 10),

    ("BACKGROUND", (0,1), (-1,-1), colors.beige),

    ("GRID", (0,0), (-1,-1), 1, colors.black),

    ("ALIGN", (0,0), (-1,-1), "CENTER"),

    ("FONTSIZE", (0,0), (-1,-1), 10),
]))

    conteudo.append(tabela)


    conteudo.append(Spacer(1,20))

    grafico = Image(caminho_grafico)
    grafico.drawWidth = 450
    grafico.drawHeight = 270

    conteudo.append(grafico)

    pdf.build(conteudo)

    if os.path.exists(caminho_grafico):
        os.remove(caminho_grafico)
    

print("PDF criado com sucesso!")