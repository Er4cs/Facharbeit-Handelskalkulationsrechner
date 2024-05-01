import tkinter as tk
from backend import Verkaufskalkulation

class VerkaufskalkulationGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Verkaufskalkulation")

        # Eingabefelder
        tk.Label(master, text="Listenpreis:").grid(row=0, column=0)
        self.listeneinkaufspreis_entry = tk.Entry(master)
        self.listeneinkaufspreis_entry.grid(row=0, column=1)

        tk.Label(master, text="Lieferrabatt:").grid(row=1, column=0)
        self.lieferrabatt_entry = tk.Entry(master)
        self.lieferrabatt_entry.grid(row=1, column=1)

        tk.Label(master, text="Lieferkonto:").grid(row=2, column=0)
        self.lieferkonto_entry = tk.Entry(master)
        self.lieferkonto_entry.grid(row=2, column=1)

        tk.Label