import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("500x500")

tk.Label(janela, text="Formulário", font=("Arial", 15, "bold")).place(x=200, y=0)
tk.Label(janela, text="Nome", font=("Arial", 10)).place(x=100, y=50)
entrada_nome = tk.Entry(janela, font=("Arial", 10), width=22)
entrada_nome.place(x=50, y=70)

tk.Label(janela, text="Sobrenome", font=("Arial", 10)).place(x=90, y=90)
entrada_sobrenome = tk.Entry(janela, font=("Arial", 10), width=22)
entrada_sobrenome.place(x=50, y=110)

tk.Label(janela, text="Data de nascimento", font=("Arial", 10)).place(x=70, y=130)
entrada_data_nasc = tk.Entry(janela, font=("Arial", 10), width=22)
entrada_data_nasc.place(x=50, y=150)

tk.Label(janela, text="CPF", font=("Arial", 10)).place(x=110, y=170)
entrada_cpf = tk.Entry(janela, font=("Arial", 10), width=22)
entrada_cpf.place(x=50, y=190)


tk.Label(janela, text="CEP", font=("Arial", 10)).place(x=110, y=210)
entrada_cep = tk.Entry(janela, font=("Arial", 10), width=22)
entrada_cep.place(x=50, y=230)

opcao = tk.IntVar()

tk.Label(janela, text="Sexo:", font=("Arial", 10)).place(x=50, y=270)
opc1 = tk.Radiobutton(janela, text="Masculino",  font=("Arial", 10), value=1,variable=opcao)\
      .place(x=90, y=290)
opc2 = tk.Radiobutton(janela, text="Feminino",  font=("Arial", 10), value=2,variable=opcao)\
      .place(x=90, y=310)
opc3 = tk.Radiobutton(janela, text="Outro",  font=("Arial", 10), value=3,variable=opcao)\
      .place(x=90, y=330)

entrada_estado = ttk.Combobox(janela, values=["MG", "RJ", "RS", "RN", "SP","AC","AL","AM","BA","CE","DF","ES","GO","MA","MT","PA","PB","PR","PI","PE","RO","RR","SC","SE","TO"])
entrada_estado.set("Selecione um estado")
entrada_estado.place(x=50, y=360)

tk.Label(janela, text="Cidade", font=("Arial", 10)).place(x=100, y=390)
entrada_cidade = tk.Entry(janela, font=("Arial", 10))
entrada_cidade.place(x=50, y=410)

def clicar():
    nome = entrada_nome.get()
    sobrenome = entrada_sobrenome.get()
    nasc = entrada_data_nasc.get()
    cpf = entrada_cpf.get()
    cep = entrada_cep.get()
    estado = entrada_estado.get()
    if opcao.get() == 1:
        sexo = "Masculino"
    elif opcao.get() == 2:
        sexo = "Feminino"
    elif opcao.get() == 3:
        sexo = "Outro"
    
    cidade = entrada_cidade.get()
    messagebox.showinfo("Mensagem: ",f"Nome: {nome}, Sobrenome: {sobrenome}, Nascido em: {nasc}, CPF: {cpf}, CEP: {cep}, Sexo: {sexo}, Estado: {estado}, Cidade: {cidade}.")
btn = tk.Button(janela, text="Enviar formulário", command=clicar)
btn.place(x=80, y=450)

janela.mainloop()






















janela.mainloop()