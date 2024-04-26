import tkinter as tk
from tkinter import ttk

class InputTable(tk.Frame):
    def __init__(self, master, headers, rows):
        super().__init__(master)
        self.headers = headers
        self.rows = rows
        self.create_widgets()

    def create_widgets(self):
        # Erstelle Kopfzeile
        for i, header in enumerate(self.headers):
            label = ttk.Label(self, text=header, borderwidth=1, relief="solid", padding=5)
            label.grid(row=0, column=i, sticky="nsew")

        # Tabelleninhalt
        table_data = [
            ["Listeneinkaufspreis", "", ""],
            ["- Lieferantenrabatt", "", ""],
            ["= Zieleinkaufspreis", "", ""],
            ["- Lieferantenskonto", "", ""],
            ["= Bareinkaufspreis", "", ""],
            ["+ Bezugskosten", "", ""],
            ["= Bezugspreis", "", ""]
        ]

        # Erstelle Eingabefelder für Datenzeilen
        self.entries = []
        for i, row in enumerate(table_data):
            row_entries = []
            for j, value in enumerate(row):
                entry = tk.Entry(self, borderwidth=1, relief="solid")
                entry.insert(tk.END, value)
                entry.grid(row=i+1, column=j, sticky="nsew")
                row_entries.append(entry)
                if i in [1, 3, 5] and j == 1:
                    entry.config(bg="pink")  # Farblich hervorheben
            self.entries.append(row_entries)

        # Konfiguriere die Zeilen- und Spalten-Größenanpassung
        self.grid_columnconfigure(0, weight=1)
        for i in range(len(self.headers)):
            self.grid_columnconfigure(i, weight=1, minsize=150)

    def calculate(self):
        try:
            # Wert aus Zeile 1, Spalte 2 (Listeneinkaufspreis in €)
            listeneinkaufspreis = float(self.entries[0][1].get().replace("€", "").replace(",", "."))

            # Wert aus Zeile 2, Spalte 1 (Lieferantenrabatt in %)
            lieferantenrabatt = float(self.entries[1][1].get().replace("%", "")) / 100

            # Wert aus Zeile 3, Spalte 1 (Lieferantenskonto in %)
            lieferantenskonto = float(self.entries[3][1].get().replace("%", "")) / 100

            # Wert aus Zeile 6, Spalte 1 (Bezugskosten in €)
            bezugskosten = float(self.entries[5][1].get().replace("€", "").replace(",", "."))

            # Berechnungen
            zieleinkaufspreis = listeneinkaufspreis - (listeneinkaufspreis * lieferantenrabatt)
            bareinkaufspreis = zieleinkaufspreis - (zieleinkaufspreis * lieferantenskonto)
            handelskalkulation = bareinkaufspreis + bezugskosten
            bezugspreis = bareinkaufspreis + bezugskosten

            # Aktualisieren der Ergebnisfelder
            self.entries[2][2].delete(0, tk.END)
            self.entries[2][2].insert(0, f"{zieleinkaufspreis:.2f} €")

            self.entries[4][2].delete(0, tk.END)
            self.entries[4][2].insert(0, f"{bareinkaufspreis:.2f} €")

            self.entries[6][2].delete(0, tk.END)
            self.entries[6][2].insert(0, f"{handelskalkulation:.2f} €")

            self.entries[7][2].delete(0, tk.END)
            self.entries[7][2].insert(0, f"{bezugspreis:.2f} €")
            
        except ValueError:
            pass  # Wenn eine ungültige Eingabe erfolgt, wird nichts berechnet

    def clear_entries(self):
        # Lösche alle Einträge aus der Tabelle außer der Kategorie "Listeneinkaufspreis"
        for i, row in enumerate(self.entries):
            if i == 0:
                continue  # Überspringe die Kategorie "Listeneinkaufspreis"
            for j, entry in enumerate(row):
                if j != 0:  # Überspringe die Kategorie-Zelle
                    entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    root.title("Bezugskalkulation")

    # Setze die Größe des Fensters
    window_width = 1000
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    headers = ["Kategorie", "Zuschlagssätze in %", "Handelskalkulation in €"]
    rows = 7  # Anzahl der Zeilen in der Tabelle
    table = InputTable(root, headers, rows)
    table.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=140, pady=140)

    # Frame für Buttons
    button_frame = tk.Frame(root)
    button_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=70, pady=70)

    # Button zum Berechnen
    calculate_button = ttk.Button(button_frame, text="Berechnen", command=table.calculate)
    calculate_button.grid(row=0, column=0, sticky="nsew", padx=10)

    # Button zum Löschen
    clear_button = ttk.Button(button_frame, text="Löschen", command=table.clear_entries)
    clear_button.grid(row=0, column=1, sticky="nsew", padx=10)

    # Platziere die Tabelle in der Mitte des Fensters
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
