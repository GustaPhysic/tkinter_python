import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("400x400")
#ETIQUETAS DO FORMULÁRIO
tk.Label(janela, text="Formulário de Cadastro", font=("Arial", 15, "bold")).grid(row=0, column=1)
#ETIQUETA DE DADOS PESSOAIS
tk.Label(janela, text="Dados pessoais:",font=("Arial", 10, "bold")).grid(row=1, column=0)
#ENTRADA DE TEXTO
tk.Label(janela, text="Nome:" , font=("Arial", 10)).grid(row=2,column=0)
entrada_nome = tk.Entry(janela, font=("Arial", 10), width=20)
entrada_nome.grid(row=2, column=1)
tk.Label(janela, text="Idade:" , font=("Arial", 10)).grid(row=3,column=0)
entrada_idade = tk.Entry(janela, font=("Arial"), width=5)
entrada_idade.grid(row=3, column=1)
#ETIQUETA DE DADOS PROFISSIONAIS
tk.Label(janela, text="Dados profissionais:",font=("Arial", 10, "bold")).grid(row=4, column=0)
#COMBOX
entrada_escolaridade = ttk.Combobox(janela, width=25, values=[ "Ensino Médio completo", "Ensino Médio incompleto", "Cursando Ensino Médio", "Cursando Ensino Superior"])
entrada_escolaridade.set("Selecione  sua escolaridade")
entrada_escolaridade.grid(row=5, column=1)
#RADIOBUTTON
opcao = tk.IntVar

tk.Label(janela, text="Área de Atuação:", font=("Arial", 10, "bold")).place(x=0, y=150)
tk.Radiobutton(janela, text="Técnico em Enfermagem", font=("Arial", 10), value=1, variable=opcao)\
.place(x=150, y=150)
     
tk.Radiobutton(janela, text="Técnico em Segurança do Trabalho", font=("Arial", 10), value=2, variable=opcao)\
.place(x=150, y=180)
     
tk.Radiobutton(janela, text="Técnico em Informática", font=("Arial", 10), value=3, variable=opcao)\
.place(x=150, y=210)
     
tk.Radiobutton(janela, text="Técnico em Estética", font=("Arial", 10), value=4, variable=opcao)\
.place(x=150, y=240)

def clicar():
       nome = entrada_nome.get()
       idade= entrada_idade.get()
       escolaridade = entrada_escolaridade()
     
       if opcao.get() == 1:
             area_de_atuacao = "Técnico em Enfermagem"
       elif opcao.get() == 2:
             area_de_atuacao = "Técnico em Segurança do Trabalho"
       elif opcao.get() == 3:
             area_de_atuacao = "Técnico em Informática"
       elif opcao.get() == 4:
             area_de_atuacao = "Técnico em Estética"

       messagebox.showinfo("Mensagem: ",f"Nome: {nome}, Idade: {idade}, Escolaridade:{escolaridade}, Área de Atuação:{area_de_atuacao}.")

btn = tk.Button(janela, text="Enviar formulário", command=clicar)
btn.place(x=150, y=280)

    

             
            

     



         
         
         

















janela.mainloop()