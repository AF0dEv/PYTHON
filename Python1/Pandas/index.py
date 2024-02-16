import pandas as pd


print("\n############## READ FROM EXCEL ###############\n")

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# .loc -----> localizar
# tabela.loc[linha, coluna]
# tabela.loc[linha, 'Multiplicador Imposto']
# tabela.loc[tabela['Tipo] == 'Serviço', coluna]

print("\n############## ALTERAR NO DATAFRAME ###############\n")

tabela.loc[tabela["Tipo"] == "Serviço", "Multiplicador Imposto"] = 1.5
print(tabela)

print("\n############## ALTERAR NO DATAFRAME(MULTIPLICACAO) ###############\n")

tabela["Preço Base Final"] = (
    tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]
)
print(tabela)

# GUARDAR NUM EXCEL
tabela.to_excel("ProdutosPandas.xlsx", index=False)
# CONVERTER EXCEL TO JSON
json_str = tabela.to_json()
with open("Produto.json", "w+") as file:
    file.write(json_str)

print("\n############## FATURAMENTO ###############\n")

faturamento = tabela[["Preço Base Final"]].sum()
print(faturamento)
