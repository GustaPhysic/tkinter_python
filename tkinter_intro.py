import tkinter as tk
#CRIAÇÃO DE JANELA
janela_main = tk.Tk()

janela_main.title("Minha Janela")
janela_main.configure(background="gray")
janela_main.minsize(200,200)
#janela_main.maxsize(500,500)
janela_main.geometry("500x500")

#OBJETOS EM JANELA
tk.Label(janela_main,
        text="Hello World",
        bg= "gray",
        font=("Arial", 20, "bold")
        ).pack()
tk.Label(janela_main,
        text="Gustavo Rodrigues Lawliet",
        bg= "white",
        font=("Arial", 20)
        ).pack()
#IMAGENS
imagem = tk.PhotoImage(file="att.png")
imagem = imagem.subsample(3,3)
tk.Label(janela_main, image= imagem).pack()



janela_main.mainloop()
