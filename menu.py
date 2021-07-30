import tkinter as tk


def clicar(event):
    mylabel = tk.Label(text="Botão carregado")
    mylabel.grid(column=0, row=0)

    # print("Botão carregado")


window = tk.Tk()
window.title("First APP")
window.geometry("300x200")
mylabel = tk.Label(text="My First APP")
mylabel.grid(column=0, row=0)
button = tk.Button(window, text="Botão")
button.grid(column=1, row=0)
button.bind("<Button-1>", clicar)
window.mainloop()
