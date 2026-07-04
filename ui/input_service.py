import tkinter as tk
from tkinter import simpledialog, messagebox

def obter_aba():
    root = tk.Tk()
    root.withdraw()

    while True:
        aba = simpledialog.askstring(
            "Gerador de Relatórios",
            "Digite a aba da planilha (ex.: 07.26):"
        )

        if aba is None:
            return None

        aba = aba.strip()

        if len(aba) == 5 and aba[2] == ".":
            root.destroy()
            return aba

        messagebox.showerror(
            "Erro",
            "Formato inválido.\nExemplo: 01.26"
        )