import tkinter as tk
from math import *


root = tk.Tk()


root.title("Calc")
root.geometry("200x400")


def somar():
    n1 = float(label1.get())
    n2 = float(label2.get())
    resultado = n1 + n2
    resultado_label['text'] = resultado
    

def subtrair():
    n1 = float(label1.get())
    n2 = float(label2.get())
    resultado = n1 - n2
    resultado_label['text'] = resultado
    

def multiplicar():
    n1 = float(label1.get())
    n2 = float(label2.get())
    resultado = n1 * n2
    resultado_label['text'] = resultado
    

def dividir():
    n1 = float(label1.get())
    n2 = float(label2.get())
    resultado = n1 / n2
    resultado_label['text'] = resultado
    

def sqrt():
    n1 = float(label1.get())
    n2 = float(label2.get())
    resultado = n1 ** n2
    resultado_label['text'] = resultado
    
    

def limpar():
    label1.delete(0, 'end')
    label2.delete(0, 'end')
    resultado_label['text'] = "Afonso Figueiredo Nº1"
    
    

# Cria os widgets
label1 = tk.Label(root, text="Numero 1:")
label1 = tk.Entry(root)
label2 = tk.Label(root, text="Numero 2:")
label2 = tk.Entry(root)
botao_somar = tk.Button(root, text=" + ", command=somar)
botao_subtrair = tk.Button(root, text=" - ", command=subtrair)
botao_multiplicar = tk.Button(root, text=" * ", command=multiplicar)
botao_dividir = tk.Button(root, text=" \ ", command=dividir)
botao_sqrt = tk.Button(root, text="sqrt", command=sqrt)
botao_limpar = tk.Button(root, text="Limpar", command=limpar)
resultado_label = tk.Label(root, text="Resultado")

# Posiciona os widgets na janela
label1.grid(row=0, column=0)
label1.grid(row=0, column=1)
label2.grid(row=1, column=0)
label2.grid(row=1, column=1)
botao_somar.grid(row=2, column=0, columnspan=5, pady=10)
botao_subtrair.grid(row=3, column=0, columnspan=5, pady=10)
botao_multiplicar.grid(row=4, column=0, columnspan=5, pady=10)
botao_dividir.grid(row=5, column=0, columnspan=5, pady=10)
botao_sqrt.grid(row=6, column=0, columnspan=5, pady=10)
botao_limpar.grid(row=7, column=0, pady=10)
resultado_label.grid(row=8, column=0, columnspan=5)

# Inicia o loop principal da janela
root.mainloop()