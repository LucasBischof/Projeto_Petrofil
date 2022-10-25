from tkinter import *
from tkinter import Tk, ttk
import datetime as dt
import mysql.connector
from tkinter import messagebox

import numpy as np

conexao = mysql.connector.connect(
 host='localhost',
 user='root',
 password='lbe04061998',
 database='banco',)
cursor = conexao.cursor()

cor0 = "#000000"  # Preta / black
cor1 = "#00009C"  # azul escuro
cor2 = "#2e2e2e"  # cinza escuro



def acessar_login():

   if e_cpf.get()!='':
    cpf_dig = int(e_cpf.get())
    cursor = conexao.cursor()
    comando = "SELECT * FROM banco.clientes_petrofil where CPF like '%" + e_cpf.get() + "%'"
    cursor.execute(comando)
    resultados = cursor.fetchall()
    print(resultados)
    if resultados==[]:
        messagebox.showinfo(title="ERRO", message="CPF incorreto")

    for resultado in resultados:
        nome_base =str(resultado[1])
        cpf_base = int(resultado[2])

        if cpf_base== cpf_dig:

            messagebox.showinfo(title="Acesso", message="Seja Bem Vindo "+nome_base)

            def voltar():
                janela_menu.destroy()

            janela_menu = Toplevel()
            janela_menu.title('Petrofil')
            janela_menu.geometry('600x600')
            janela_menu.configure(background=cor0)
            janela_menu.resizable(width=False, height=False)
            janela_menu.transient(janela_login)
            janela_menu.focus_force()
            janela_menu.grab_set()

            frame_cima = Frame(janela_menu, width=700, height=100, bg=cor0, relief='flat')
            frame_cima.grid(row=0, columnspan=1, pady=1, padx=0, sticky=NSEW)

            frame_baixo = Frame(janela_menu, width=700, height=450, bg=cor0, relief='flat')
            frame_baixo.grid(row=1, columnspan=1, pady=1, padx=0, sticky=NSEW)

        # Configurando o frame Cima ----------------------

            tipo_cad = Label(frame_cima, text='Tipo de Combustivel', bg=cor0, fg=cor1, font=('ivy 18 bold'))
            tipo_cad.place(x=20, y=5)

            label_imagem = Label(janela_menu, image=img)
            label_imagem.place(x=220, y=400 )

            tipo_cad_linha = Label(frame_cima, text='', width=450, anchor=NW, font=('ivy 1'), bg=cor2, fg=cor1)
            tipo_cad_linha.place(x=10, y=45)

            msg_tx = Label(frame_cima, text='Escolha o Combustivel, Voce tem 10% de Desconto', bg=cor0, fg=cor1, font=('ivy 12'))
            msg_tx.place(x=10, y=80)

        # Configurando o frame baixo ----------------------

            b_cadastrar_produtos = Button(frame_baixo, text='Álcool', width=40, height=1, bg=cor2, fg=cor1,
                           font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
            b_cadastrar_produtos.place(x=60, y=50)

            b_preco_combustivel = Button(frame_baixo, text='Gasolina Comum', width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
            b_preco_combustivel.place(x=60, y=110)

            b_cadastrar_usuario = Button(frame_baixo, text='Gasolina Aditivada', width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
            b_cadastrar_usuario.place(x=60, y=170)

            b_voltar = Button(frame_baixo, text='Voltar',command=voltar, width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
            b_voltar.place(x=60, y=230)
        else:
            messagebox.showinfo(title="ERRO", message="CPF incorreto")
   else:

         messagebox.showinfo(title="ERRO", message="Digite o CPF")

def continuar():

        messagebox.showinfo(title="Login", message="Seja bem Vindo")
        def voltar():
            janela_menu.destroy()

        janela_menu = Toplevel()
        janela_menu.title('Petrofil')
        janela_menu.geometry('600x600')
        janela_menu.configure(background=cor0)
        janela_menu.resizable(width=False, height=False)
        janela_menu.transient(janela_login)
        janela_menu.focus_force()
        janela_menu.grab_set()

        frame_cima = Frame(janela_menu, width=700, height=100, bg=cor0, relief='flat')
        frame_cima.grid(row=0, columnspan=1, pady=1, padx=0, sticky=NSEW)

        frame_baixo = Frame(janela_menu, width=700, height=450, bg=cor0, relief='flat')
        frame_baixo.grid(row=1, columnspan=1, pady=1, padx=0, sticky=NSEW)

        # Configurando o frame Cima ----------------------

        tipo_cad = Label(frame_cima, text='Tipo de Combustivel', bg=cor0, fg=cor1, font=('ivy 18 bold'))
        tipo_cad.place(x=20, y=5)

        label_imagem = Label(janela_menu, image=img)
        label_imagem.place(x=220, y=400 )

        tipo_cad_linha = Label(frame_cima, text='', width=450, anchor=NW, font=('ivy 1'), bg=cor2, fg=cor1)
        tipo_cad_linha.place(x=10, y=45)

        msg_tx = Label(frame_cima, text='Escolha o Combustivel', bg=cor0, fg=cor1, font=('ivy 12'))
        msg_tx.place(x=10, y=80)

        # Configurando o frame baixo ----------------------

        b_cadastrar_produtos = Button(frame_baixo, text='Álcool', width=40, height=1, bg=cor2, fg=cor1,
                           font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
        b_cadastrar_produtos.place(x=60, y=50)

        b_preco_combustivel = Button(frame_baixo, text='Gasolina Comum', width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
        b_preco_combustivel.place(x=60, y=110)

        b_cadastrar_usuario = Button(frame_baixo, text='Gasolina Aditivada', width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
        b_cadastrar_usuario.place(x=60, y=170)

        b_voltar = Button(frame_baixo, text='Voltar',command=voltar, width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
        b_voltar.place(x=60, y=230)



# Criando a janela-------------------------

janela_login = Tk()
janela_login.title('Petrofil')
janela_login.geometry('600x600')
janela_login.configure(background=cor0)
janela_login.resizable(width=False, height=False)

img = PhotoImage(file='C:\\Users\Infoprice\Desktop\Petrofil\\logo.png')
janela_login.iconphoto(False, img)




# Dividindo a janela ----------------------

frame_cima = Frame(janela_login , width=700, height=150, bg=cor0, relief='flat')
frame_cima.grid(row=0, columnspan=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela_login, width=700, height=450, bg=cor0, relief='flat')
frame_baixo.grid(row=1, columnspan=1, pady=1, padx=0, sticky=NSEW)

# Configurando o frame Cima ----------------------

tipo_cad = Label(frame_cima, text='Login Fidelidade', bg=cor0, fg=cor1, font=('ivy 18 bold'))
tipo_cad.place(x=20, y=5)

label_imagem = Label(janela_login, image=img)
label_imagem.place(x=220,y=360,)

tipo_cad_linha = Label(frame_cima, text='',width=450, anchor=NW,font=('ivy 1'), bg=cor2, fg=cor1)
tipo_cad_linha.place(x=10, y=45)


cpf_txt = Label(frame_baixo, text='CPF: ', bg=cor0, fg=cor1, font=('ivy 15'))
cpf_txt.place(x=20, y=50)

e_cpf = Entry(frame_baixo, width=15, bd=1, font=('ivy 15'))
e_cpf.place(x=100, y=50)

# Configurando o frame baixo-----------------------


b_acessar =Button(frame_baixo,command=acessar_login, text='Acessar',width=20,height=1, bg=cor2, fg=cor1, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_acessar.place(x=350, y=50)


msg_tx = Label(frame_cima, text='Acesse o Clube fidelidade ou Continue o abastecimento Sem os benefícios', bg=cor0, fg=cor1, font=('ivy 12'))
msg_tx.place(x=20, y=120)

msg2_tx = Label(frame_cima, text='Seja Bem Vindo Ao Posto Petrofil ', bg=cor0, fg=cor1, font=('ivy 12'))
msg2_tx.place(x=20, y=80)

b_continuar =Button(frame_cima,command=continuar, text='Continuar Sem Login',width=20,height=1, bg=cor2, fg=cor1, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_continuar.place(x=290, y=80)


janela_login.mainloop()
