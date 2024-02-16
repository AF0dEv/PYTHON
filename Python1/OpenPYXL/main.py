from openpyxl import load_workbook, Workbook

tabela = load_workbook("Produtos.xlsx")
ative_sep = tabela.active

for celula in ative_sep["C"]:
    if celula.value == "Serviço":
        linha = celula.row
        ative_sep[f"D{linha}"] = 1.5
    if celula.value == "Produto":
        linha = celula.row
        ative_sep[f"D{linha}"] = 1.3

tabela.save("ProdutosOPENPYXL.xlsx")
