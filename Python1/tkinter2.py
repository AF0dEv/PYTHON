from tkinter import *
from tkinter import ttk

cor1 = '#000000' # Preto
cor2 = '#ffffff' # Branco
cor3 = '#0000ff' # Azul
cor4 = '#373737' # Cinzento Escuro
cor5 = '#00ff00' # Verde 

# Criação Janela
janela = Tk()
janela.title ('Afonso Calculadora')

janela.geometry('235x318')


# Criação Frames

frame_visor = Frame(janela, width=235, height=50, bg=cor3)
frame_visor.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor5)
frame_corpo.grid(row=1, column=0)

# Criar Botões

btn1 = Button(frame_corpo, text='C', width=11, height=2, bg = cor4, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN)
btn1.place(x=0,y=0)


btn2 = Button(frame_corpo, text='%', width=7, height=2, bg = cor3, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN)
btn2.place(x=116,y=0)


btn3 = Button(frame_corpo, text='/', width=7, height=2, bg = cor3, font='Ivy 13 bold', relief=RAISED, overrelief=SUNKEN)
btn3.place(x=176,y=0)


# Criar Label

app_label = Label(frame_visor, text='123456789', width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font='Ivy 18', bg=cor1, fg=cor5)

app_label.place(x=0, y=0)

'''
#Criar ComboBox

cbx1 = ttk.Combobox(frame_corpo, values='Subtrair Somar')
cbx1.place(x=0, y=200)
'''



















janela.mainloop()