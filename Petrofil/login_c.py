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
    if e_nome.get() != '' and e_senha.get()!='':

        nome_dig = str(e_nome.get())
        senha_dig = str(e_senha.get())
        cursor = conexao.cursor()
        comando = "SELECT * FROM banco.funcionarios_petrofil where nome like '%" + nome_dig + "%'"
        cursor.execute(comando)
        resultados = cursor.fetchall()
        print(resultados)
        for resultado in resultados:
            nome_base = str(resultado[1])
            senha_base = str(resultado[2])
            cargo_base =  str(resultado[3])

            if nome_base == nome_dig and senha_base == senha_dig:

             if cargo_base == "gerente":

              messagebox.showinfo(title="Acesso", message="Seja Bem Vindo " + nome_base)


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

              tipo_cad = Label(frame_cima, text='Menu principal', bg=cor0, fg=cor1, font=('ivy 18 bold'))
              tipo_cad.place(x=20, y=5)

              label_imagem = Label(janela_menu, image=img)
              label_imagem.place(x=220, y=400 )

              tipo_cad_linha = Label(frame_cima, text='', width=450, anchor=NW, font=('ivy 1'), bg=cor2, fg=cor1)
              tipo_cad_linha.place(x=10, y=45)

        # Configurando o frame baixo ----------------------

              b_cadastrar_produtos = Button(frame_baixo, text='Cadastro de Produtos', width=40, height=1, bg=cor2, fg=cor1,
                           font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
              b_cadastrar_produtos.place(x=60, y=50)

              b_preco_combustivel = Button(frame_baixo, text='Atualização de preço de Combustivel', width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
              b_preco_combustivel.place(x=60, y=110)

              b_cadastrar_usuario = Button(frame_baixo, text='Cadastro de Usuarios', width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
              b_cadastrar_usuario.place(x=60, y=170)

              b_voltar = Button(frame_baixo, text='Voltar',command=voltar, width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
              b_voltar.place(x=60, y=230)

             elif cargo_base == "vendedor":
                messagebox.showinfo(title="Login", message="Seja bem Vindo Joao")
                janela_menu_consulta = Toplevel()
                janela_menu_consulta.title('Petrofil')
                janela_menu_consulta.geometry('600x600')
                janela_menu_consulta.configure(background=cor0)
                janela_menu_consulta.resizable(width=False, height=False)
                janela_menu_consulta.transient(janela_login)
                janela_menu_consulta.focus_force()
                janela_menu_consulta.grab_set()

                def voltar():
                 janela_menu_consulta.destroy()

                frame_cima = Frame(janela_menu_consulta, width=700, height=100, bg=cor0, relief='flat')
                frame_cima.grid(row=0, columnspan=1, pady=1, padx=0, sticky=NSEW)

                frame_baixo = Frame(janela_menu_consulta, width=700, height=450, bg=cor0, relief='flat')
                frame_baixo.grid(row=1, columnspan=1, pady=1, padx=0, sticky=NSEW)

        # Configurando o frame Cima ----------------------

                tipo_cad = Label(frame_cima, text='Menu Consulta', bg=cor0, fg=cor1, font=('ivy 18 bold'))
                tipo_cad.place(x=20, y=5)

                label_imagem = Label(janela_menu_consulta, image=img)
                label_imagem.place(x=220, y=400, )

                tipo_cad_linha = Label(frame_cima, text='', width=450, anchor=NW, font=('ivy 1'), bg=cor2, fg=cor1)
                tipo_cad_linha.place(x=10, y=45)

                b_venda = Button(frame_baixo, text='Vendas', width=40, height=1, bg=cor2, fg=cor1,
                                      font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
                b_venda.place(x=60, y=50)

                b_consultar_produtos = Button(frame_baixo, text='Consultar Produtos', width=40, height=1,
                                     bg=cor2, fg=cor1,
                                     font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
                b_consultar_produtos.place(x=60, y=110)

                b_cadastrar_clientes = Button(frame_baixo, text='Cadastro de cliente', width=40, height=1, bg=cor2, fg=cor1,
                                     font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
                b_cadastrar_clientes.place(x=60, y=170)

                b_voltar = Button(frame_baixo, text='Voltar', command=voltar, width=40, height=1, bg=cor2, fg=cor1,
                          font=('ivy 15 bold'), relief=RAISED, overrelief=RIDGE)
                b_voltar.place(x=60, y=230)
             else:
                messagebox.showinfo(title="ERRO", message="Usuario ou senha incorreto")
            else:
             messagebox.showinfo(title="ERRO", message="Usuario ou senha incorreto")
    else:
                    messagebox.showinfo(title="ERRO", message="Usuario ou senha incorreto")

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

tipo_cad = Label(frame_cima, text='Login Conveniencia ', bg=cor0, fg=cor1, font=('ivy 18 bold'))
tipo_cad.place(x=20, y=5)

label_imagem = Label(janela_login, image=img)
label_imagem.place(x=220,y=360,)

tipo_cad_linha = Label(frame_cima, text='',width=450, anchor=NW,font=('ivy 1'), bg=cor2, fg=cor1)
tipo_cad_linha.place(x=10, y=45)

nome_txt = Label(frame_baixo, text='Nome: ', bg=cor0, fg=cor1, font=('ivy 15'))
nome_txt.place(x=20, y=20)

e_nome = Entry(frame_baixo, width=15, bd=1, font=('ivy 15'))
e_nome.place(x=100, y=20)

senha_txt = Label(frame_baixo, text='Senha: ', bg=cor0, fg=cor1, font=('ivy 15'))
senha_txt.place(x=20, y=50)

e_senha = Entry(frame_baixo,show='*', width=15, bd=1, font=('ivy 15'))
e_senha.place(x=100, y=50)

# Configurando o frame baixo-----------------------


b_acessar =Button(frame_baixo,command=acessar_login, text='Acessar',width=20,height=1, bg=cor2, fg=cor1, font=('ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
b_acessar.place(x=350, y=50)


cliente_tx = Label(frame_cima, text='Digite o Nome e a Senha para fazer o login', bg=cor0, fg=cor1, font=('ivy 12'))
cliente_tx.place(x=10, y=80)


janela_login.mainloop()
