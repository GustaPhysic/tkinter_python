import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("500x300")
janela.configure(background="gray")

tk.Label(janela, text="Formulário", font=("Arial", 15, "bold"), bg="gray").place(x=200, y=0)
#ENTRADA DE DADOS
tk.Label(janela, text="Usuário", font=("Arial", 10, "bold"), bg= "gray").place(x=120, y=50)
entrada_nome = tk.Entry(janela, font=("Arial", 10), bd= 4, width=25)
entrada_nome.place(x=60, y=70)
tk.Label(janela, text="Senha", font=("Arial", 10, "bold"), bg="gray").place(x=120, y=100)
entrada_senha = tk.Entry(janela, font=("Arial", 10), bd= 4, width=25)
entrada_senha.place(x=60, y=120)

def clicar():
    messagebox.showinfo("AVISO", "Usuário logado com sucesso")

btn = tk.Button(janela, text="Confirmar", command=clicar)
btn.place(x=100, y=180)    

imagem = tk.PhotoImage(file="l.png")
imagem = imagem.subsample(3,3)
tk.Label(janela, image= imagem).place(x=250, y=50)



  











janela.mainloop()

