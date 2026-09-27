
# 📊 Pipeline ETL de Vendas (Brasil)

Pipeline de Extração, Transformação e Carga (ETL) desenvolvido em **Python** utilizando a biblioteca **Pandas** para processar bases de dados de vendas de lojas brasileiras, preparando os dados para análises de negócios (BI) e futuras integrações com dashboards interativos.

---

## 🚀 Funcionalidades e Métricas Calculadas

O script processa a planilha bruta e retorna um dicionário estruturado contendo os seguintes indicadores (KPIs):

* **Faturamento Total e por Loja:** Agrupamento e ordenação decrescente do desempenho financeiro das filiais.
* **Ticket Médio:** Cálculo geral e segmentado por ID de loja.
* **Análise de Produtos:** Identificação do volume de vendas por produto e por loja, além de um ranking global dos itens mais vendidos.
* **Evolução Diária:** Agrupamento cronológico do faturamento por data.
* **Comportamento do Cliente:** Identificação do ranking dos clientes que mais geram receita.
* **Destaques Automáticos:** Extração automática dos principais highlights do negócio (`iloc[0]`) para alimentação rápida de *cards* em dashboards.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas** (Manipulação e tratamento de dados)
* **Openpyxl** (Leitura de arquivos Excel)

---

## ⚙️ Como Executar

1. **Pré-requisitos:** Certifique-se de ter o Python instalado junto com as bibliotecas necessárias:
   ```bash
   pip install pandas openpyxl
   ```
