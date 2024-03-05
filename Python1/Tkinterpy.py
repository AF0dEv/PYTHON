from tkinter import *
# Criação Objeto <-- Tk é um Construtor
menu_inicial = Tk()

menu_inicial.title('O meu 1º TKinter')
'''
#       largura x altura / posiçao x / posiçao y
menu_inicial.geometry('500x300+300+0')

#                   largura / altura
menu_inicial.resizable(True, True)

menu_inicial.minsize(width=500, height=250)
menu_inicial.maxsize(width=700, height=500)

'''
menu_inicial.geometry('500x250')
'''
menu_inicial.state('zoomed') # abre a janela maximizada
'''
menu_inicial.state('iconic') # abre a janela e minimiza

# menu_inicial.iconbitmap('AnyConv.com__icone.icns')


# mainloop mantem aplicação aberta
menu_inicial.mainloop()
