import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


def executar_etl(caminho_excel="vendas_lojas_brasil.xlsx", exportar_csv=False):

    tabela = pd.read_excel(caminho_excel)

    # Garante que "Data" seja datetime de verdade
    tabela["Data"] = pd.to_datetime(tabela["Data"], errors="coerce").dt.normalize()

    # Padroniza o nome da loja (cidade) — Title Case
    tabela["ID Loja"] = tabela["ID Loja"].str.strip().str.title()

    # ---------- FATURAMENTO TOTAL / POR LOJA ----------
    faturamento_total = tabela["Valor Final"].sum()

    faturamento_loja = (
        tabela[["ID Loja", "Valor Final"]]
        .groupby("ID Loja").sum()
        .sort_values(by="Valor Final", ascending=False)
        .reset_index()
    )

    # ----------------- TICKET MÉDIO ------------------------
    ticket_medio = tabela["Valor Final"].mean()

    ticket_medio_loja = (
        tabela.groupby("ID Loja")["Valor Final"].mean()
        .reset_index()
        .sort_values(by="Valor Final", ascending=False)
    )

    # ------------------- PRODUTO MAIS VENDIDO -----------------------
    produto_mais_vendido = (
        tabela[["ID Loja", "Produto", "Quantidade", "Valor Final"]]
        .groupby(["ID Loja", "Produto"]).sum()
        .reset_index()
    )

    # Ranking global de produtos (para o gráfico)
    ranking_produtos = (
        tabela[["Produto", "Quantidade"]]
        .groupby("Produto").sum()
        .sort_values(by="Quantidade", ascending=False)
        .head(10)
        .reset_index()
    )

    # -------------------------- VOLUME TOTAL DE ITENS --------------------------------
    total_itens_vendido = tabela["Quantidade"].sum()

    # ------------------- FATURAMENTO DIARIO -----------------
    faturamento_diario = (
        tabela[["Data", "Valor Final"]]
        .groupby("Data").sum()
        .reset_index()
        .sort_values(by="Data")
    )

    # -------------------- CLIENTES QUE MAIS COMPRAM -----------------------------
    clientes_que_mais_gastam = (
        tabela[["Cliente", "Valor Final"]]
        .groupby("Cliente").sum()
        .reset_index()
        .sort_values(by="Valor Final", ascending=False)
    )

    # -------------------- DESTAQUES (para os cards) --------------------
    # .iloc[0] → pega a linha na POSIÇÃO 0 (a primeira).
    #   Como os DataFrames já estão ordenados de forma DECRESCENTE,
    #   a linha 0 é o MAIOR valor de cada ranking.
    loja_que_mais_vende = faturamento_loja.iloc[0].to_dict()
    cliente_que_mais_compra = clientes_que_mais_gastam.iloc[0].to_dict()
    item_mais_vendido = ranking_produtos.iloc[0].to_dict()

    return {
        "tabela_original": tabela,
        "faturamento_total": faturamento_total,
        "faturamento_loja": faturamento_loja,
        "faturamento_diario": faturamento_diario,
        "ticket_medio": ticket_medio,
        "ticket_medio_loja": ticket_medio_loja,
        "produto_mais_vendido": produto_mais_vendido,
        "ranking_produtos": ranking_produtos,
        "volume_itens": total_itens_vendido,
        "clientes_que_mais_gastam": clientes_que_mais_gastam,
        "loja_que_mais_vende": loja_que_mais_vende,
        "cliente_que_mais_compra": cliente_que_mais_compra,
        "item_mais_vendido": item_mais_vendido,
    }