import tkinter as tk
from tkinter import PhotoImage

def set_logo(window):
    logo_image = PhotoImage(file="C:\Users\ericn\Facharbeit-Handelskalkulationsrechner-1\logo.jpg")  # Passe den Pfad zu deinem Logo an
    window.iconphoto(False, logo_image)

# Erstellen eines Tkinter-Fensters
root = tk.Tk()
root.title("Mein Fenster")

# Setze das Logo auf das Hauptfenster
set_logo(root)

# Füge Widgets hinzu ...
label = tk.Label(root, text="Hallo Welt!")
label.pack()

root.mainloop()
