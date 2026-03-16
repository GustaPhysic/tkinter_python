import tkinter as tk
#CRIAÇÃO DE JANELA
janela_main = tk.Tk()

janela_main.title("Símbolo a Tropa de Exploração")
janela_main.configure(background="black")
janela_main.minsize(200,200)
#janela_main.maxsize(800,800)
janela_main.geometry("800x800")

#OBJETOS EM JANELA
tk.Label(janela_main,
        text="Símbolo da Tropa de Exploração AOT",
        bg= "blue",
        font=("Arial", 20, "bold")
        ).pack()
tk.Label(janela_main,
        text="Escudo que fica no manto dos caçadores de titans no anime Attack On Titan",
        bg= "green",
        font=("Arial", 15)
        ).pack()
#IMAGENS
imagem = tk.PhotoImage(file="aot2.png")
imagem = imagem.zoom(1,1)
tk.Label(janela_main, image= imagem).pack()



janela_main.mainloop()
