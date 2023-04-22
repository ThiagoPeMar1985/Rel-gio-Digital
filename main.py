import tkinter as tk
from tkinter import *
import os
from time import strftime



root = tk.Tk()
root.title('Relogio digital')
root.geometry('400x200')
root.minsize(400, 200)
root.configure(background="#000000")

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text="Olá, "  + nome_usuario)
    
def get_data():
    data_atual=strftime("%A,%d %b %Y")    
    data.config(text=data_atual)
    
def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000,get_horas)
    
tela = tk.Canvas(root, width=500, height=30,bg="#000000", bd=0, highlightthickness=0, relief='ridge')
tela.pack()
    
saudacao = Label(root,bg='#000000',fg='#C0C0C0',font=('Montserrat', 16))
saudacao.pack()

data = Label(root,bg='#000000',fg='#C0C0C0',font=('Montserrat', 14))
data.pack(pady=2)

horas = Label(root,bg='#000000',fg='#C0C0C0',font=('Montserrat', 64, 'bold'))
horas.pack(pady=2)
get_saudacao()
get_data()
get_horas()


root.mainloop()