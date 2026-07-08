from services.sheets_service import listar_abas, ler_planilha
from services.analise_service import calcular_renovacoes_geral


def comparar_renovacoes_meses(nome_planilha):

    resultado = []

    abas = listar_abas(nome_planilha)

    for aba in abas:

        # Lê a aba
        df = ler_planilha(nome_planilha, aba)

        # Calcula o resumo geral daquela aba
        resumo = calcular_renovacoes_geral(df)

        # Guarda o resultado
        resultado.append({
            "mes": aba,
            "total": resumo["total"],
            "renovaram": resumo["renovaram"],
            "nao": resumo["nao"],
            "perc_renovaram": resumo["perc_renovaram"],
            "perc_nao": resumo["perc_nao"]
        })

    return resultado