from tkinter import *
from tkinter import ttk

# Cores, Hexadecimal, Nome
cor1 = '#000000' # Preto
cor2 = '#ffffff' # Branco
cor3 = '#0000ff' # Azul
cor4 = '#373737' # Cinzento Escuro
cor5 = '#00ff00' # Verde 

# Criação Janela
janela = Tk()

# Título da Janela
janela.title ('Afonso Calculadora')

# Tamanho da Janela
janela.geometry('235x318')


# Criação Frames

# Frame Visor, tamanho 235x50, cor de fundo Azul
frame_visor = Frame(janela, width=235, height=50, bg=cor3)
# Posição do Frame Visor
frame_visor.grid(row=0, column=0)

# Frame Corpo, tamanho 235x268, cor de fundo Cinzento Escuro
frame_corpo = Frame(janela, width=235, height=268)
# Posição do Frame Corpo
frame_corpo.grid(row=1, column=0)

# Criar Label

# Label Visor, tamanho 16x2, cor de fundo Azul, cor da letra Verde
app_label = Label(frame_visor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font='Ivy 18', bg=cor1, fg=cor5)

# Posição do Label Visor
app_label.place(x=0, y=0)

# Criar Variável Global para Expressão Matemática
expressao_mat = ""

# Funções

# Adicionar Texto â Expressão Matemática e Atualizar o Label 
def adicionarExpressao(texto):
    global expressao_mat # Global para poder ser usada dentro da função
    expressao_mat += texto
    app_label.config(text=expressao_mat)


# Calcular a Expressão Matemática e Atualizar o Label, se houver erro, mostrar "Erro"
def calcularExpressao():
    global expressao_mat
    try:
        expressao_mat = str(eval(expressao_mat)) # Eval é uma função que executa uma string como expressão matemática
    except Exception as e:
        expressao_mat = "Erro"
    app_label.config(text=expressao_mat)


# Limpar o Label e a Expressão Matemática
def limparLabel():
    global app_label, expressao_mat # Global para poder ser usada dentro da função
    app_label.destroy() # Destruir o Label
    app_label = Label(frame_visor, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font='Ivy 18', bg=cor1, fg=cor5) # Criar um novo Label
    app_label.place(x=0, y=0) # Posicionar o novo Label
    expressao_mat = ""  # Limpar a Expressão Matemática 

# Criar Números, 
for i in range(9):
    Button(frame_corpo, text=str(i+1), width=7, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda i=i: adicionarExpressao(str(i+1))).place(x=(i%3)*58, y=(i//3)*53+53) 
# i=i -> Parâmetro para a função lambda, adicionarExpressao(str(i+1)) -> Adicionar o número ao Label, place(x=(i%3)*58, y=(i//3)*53+53) -> Posicionar o botão, i%3 -> Resto da Divisão, i//3 -> Divisão Inteira, *58 e *53+53 -> Posicionamento dos botões

# Criar Botão 0
Button(frame_corpo, text='0', width=7, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda: adicionarExpressao('0')).place(x=58, y=212)

# Criar Botões de Operações
Button(frame_corpo, text='+', width=7, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda: adicionarExpressao('+')).place(x=176, y=53)
Button(frame_corpo, text='-', width=7, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda: adicionarExpressao('-')).place(x=176, y=106)
Button(frame_corpo, text='*', width=7, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda: adicionarExpressao('*')).place(x=176, y=159)
Button(frame_corpo, text='/', width=7, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda: adicionarExpressao('/')).place(x=176, y=212)

# Criar Botão de Igual
Button(frame_corpo, text='=', width=7, height=2, bg=cor3, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=calcularExpressao).place(x=116, y=212)

# Criar Botão de Ponto
Button(frame_corpo, text='.', width=7, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda: adicionarExpressao('.')).place(x=0, y=212)

# Criar Botão de Limpar
Button(frame_corpo, text='C', width=23, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN, command=lambda: limparLabel()).place(x=0, y=0)

janela.mainloop() # Manter a Janela Aberta
