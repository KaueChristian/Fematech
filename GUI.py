from tkinter import *
janela = Tk()


class Mostrar_janela():
    def __init__(self):
        self.janela = janela
        self.Tela()
        self.frames_tela()
        self.botões()
        self.textos()
        janela.mainloop()

# configuraçôes da tela exibida
    def Tela(self):
        self.janela.title("'nome do programa'")
        self.janela.configure(background='#AED6F1')
        self.janela.geometry("900x600")
        self.janela.resizable(True, True)
        self.janela.minsize(width=700, height=400)

#  Criando os frames da tela
    def frames_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg='lightgrey', highlightbackground='black', highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.26)

        self.frame_2 = Frame(self.janela, bd=4, bg='lightgrey',highlightbackground='black', highlightthickness=1)
        self.frame_2.place(relx=0.50, rely=0.02, relwidth=0.46, relheight=0.26)

        self.frame_3 = Frame(self.janela, bd=4, bg='lightgrey', highlightbackground='black', highlightthickness=1)
        self.frame_3.place(relx=0.02, rely=0.30, relwidth=0.46, relheight=0.65)

        self.frame_4 = Frame(self.janela, bd=4, bg='lightgrey', highlightbackground='black', highlightthickness=1)
        self.frame_4.place(relx=0.50, rely=0.30, relwidth=0.46, relheight=0.65)

#  Criando botões
    def botões(self):
        self.bt_gerar = Button(self.frame_1, text='Gerar',font=(8))
        self.bt_gerar.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.15)

        self.bt_gerar2 = Button(self.frame_2, text='Gerar', font=(8))
        self.bt_gerar2.place(relx=0.35, rely=0.50,relwidth=0.3, relheight=0.20)

#  Gerando as labels e entrys(Mensagens)
    def textos(self):
        
        self.texto1 = Label(self.frame_1, text='Digite uma senha para criptografar: ',bg='lightgrey', font=("Helvetica", 14))
        self.texto1.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.15)

        self.entry1 = Entry(self.frame_1, bd=1, bg='white', highlightbackground='black', highlightthickness=1)
        self.entry1.place(relx=0.05, rely=0.30, relwidth=0.90, relheight=0.15)

        self.texto2 = Label(self.frame_2, text='Não tem uma senha? CRIE AGORA !', bg='lightgrey', font=("Helvetica", 14))
        self.texto2.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.15)


Mostrar_janela()
