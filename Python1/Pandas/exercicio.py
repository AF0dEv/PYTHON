import pandas as pd


print("\n############## READ FROM EXCEL ###############\n")

tabela = pd.read_excel("Exercicio1.xlsx")
print(tabela)

print("\n--------------- TOTAL ------------------\n")
tabela["TOTAL"] = (tabela["PRECO"] * tabela["QTD"] + tabela["SERVICO"]) * tabela[
    "IMPOSTO"
]
print(tabela)

print("\n--------------- CONVERSOES ------------------\n")
tabela.loc[tabela["LOCAL"] == "Esplanada", "SERVICO"] = 1.5
tabela.loc[tabela["LOCAL"] == "Balcao", "SERVICO"] = 0.5
tabela.loc[tabela["LOCAL"] == "Mesa", "SERVICO"] = 1
tabela["TOTAL"] = (tabela["PRECO"] * tabela["QTD"] + tabela["SERVICO"]) * tabela[
    "IMPOSTO"
]
print(tabela)

faturamento = tabela[["TOTAL"]].sum()
print(faturamento)

tabela.to_excel("ExercicioPandas.xlsx", index=False)

