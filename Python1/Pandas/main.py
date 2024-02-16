# O pandas é a melhor biblioteca python para dados
# O pandas é a melhor biblioteca python para analise de dados

# A primeira coisa que tem que saber é a utilzacao do import

import pandas as pd

print("Versao Pandas ->", pd.__version__)

# O panda funciona dentro do python como um dataframe
# Um dataframe é uma tabela dentro do python

# Existem 3 formas de criar uma dataframe

# 1º forma ---> Criar um dataframe vazio
dataframe = pd.DataFrame()

# 2º forma ---> Criar um dataframe a partir de um dicionario
print("\n############## READ FROM DICIONARIO ###############\n")
venda = {
    "DATA": ["15/02/2021", "16/02/2022"],
    "VALOR": [500, 300],
    "PRODUTO": ["batata", "arroz"],
    "QTD": [50, 70],
}


# Agora vamos criar um dataframe no python a partir do dicionario
vendas_df = pd.DataFrame(venda)
print(vendas_df)

# 3º ---> Criar um dataframe a partir de um ficheiro ou base de dados
print("\n############## READ FROM EXCEL ###############\n")

vendas_ex = pd.read_excel("Vendass.xlsx")
print(vendas_ex)

# Existem 3 metodos muito uteis:
# head
# shape
# describe

# Metodo head
"""
Ele por defeito mostra somente as 5 primeiras linhas, se quisermos mais, temos que colocar
que colocar na funcao o metodo:
"""
print("\n############## HEAD ###############\n")
print(vendas_ex.head(10))

# Metedo shape
"""
Serve para mostrar quantas linhas e colunas o dataframe tem
"""
print("\n############## SHAPE ###############\n")
print(vendas_ex.shape)


# Metodo describe
"""
Mostra um resumo dos dados (apenas dados numericos) do dataframe, por total,
por media, por desvio padrao, min, max, etc
"""
print("\n############## DESCRIBE ###############\n")
print(vendas_ex.describe())


"""
edicao de dataframe
Imaginem que eu no dataframe queria pegar so em produtos
"""
print("\n############## EDICAO DATAFRAME ###############\n")
produtos = vendas_ex["Produto"]
print(produtos)

# Quando pedimos para ler uma coluna, já nao é um dataframe mas sim uma 'serie'
print("\n############## EDICAO DATAFRAME(SERIE) ###############\n")
serie = vendas_ex[["Produto", "ID Loja"]]
print(serie)

# Outros metodos
# .Loc
print("\n############## OUTROS METODOS ###############\n")
print("\n############## LOC ###############\n")
print(vendas_ex.loc[1], ["Produto"])
print("\n-----------------------------------------\n")
print(vendas_ex.loc[1:5])
print("\n--------------- VENDAS NS ------------------\n")
vendas_northShopping = vendas_ex.loc[
    vendas_ex["ID Loja"] == "Norte Shopping", ["ID Loja", "Produto", "Quantidade"]
]
print(vendas_northShopping)
print("\n--------------- 5% COMISSOES ------------------\n")
vendas_ex["Comissao"] = vendas_ex["Valor Final"] * 0.05
print(vendas_ex)
print("\n--------------- COMISSOES ACIMA DE 50 EUROS ------------------\n")
print(vendas_ex.loc[vendas_ex["Comissao"] > 50])

print("\n-----------------CRIA UMA COLUNA IMPOSTO COM VALOR ZERO-----------------\n")
# os dois pontos significam todas as linhas e se tiver outros dois é para colunas
vendas_ex.loc[:, "Imposto"] = 0
print(vendas_ex)
