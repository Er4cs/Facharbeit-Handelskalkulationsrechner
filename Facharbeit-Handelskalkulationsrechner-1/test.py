from tkinter import*

tk = Tk()
canvas = Canvas(tk, width=1000, height=600)
canvas.pack()
mein_Bild = PhotoImage(file='c:\\test.gif')
canvas.create_image(0, 0, anchor=NW, image=mein_Bild)

class InputTable(tk.Frame):
    def __init__(self, master, headers, table_data):
        super().__init__(master)
        self.headers = headers
        self.table_data = table_data
        self.create_widgets()

    def create_widgets(self):
        # Erstelle Kopfzeile
        for i, header in enumerate(self.headers):
            label = ttk.Label(self, text=header, borderwidth=1, relief="solid", padding=5)
            label.grid(row=0, column=i, sticky="nsew")

        # Erstelle Eingabefelder für Datenzeilen
        self.entries = []
        for i, row in enumerate(self.table_data):
            row_entries = []
            for j, value in enumerate(row):
                entry = tk.Entry(self, borderwidth=1, relief="solid")
                entry.insert(tk.END, value)
                entry.grid(row=i+1, column=j, sticky="nsew")
                row_entries.append(entry)
                if i in [1, 3, 5, 7] and j == 1:
                    entry.config(bg="pink")  # Farblich hervorheben
                if i == 5 and j == 1:
                    entry.config(bg="pink")  # Farblich hervorheben
                if i == 0 and j == 2:
                    entry.config(bg="red")  # Farblich hervorheben
                if i in [1, 3] and j == 2:
                    entry.config(state="disabled")  # Deaktiviere die Eingabe in den Handelskalkulationsfeldern
            self.entries.append(row_entries)

        # Konfiguriere die Zeilen- und Spalten-Größenanpassung
        self.grid_columnconfigure(0, weight=1)
        for i in range(len(self.headers)):
            self.grid_columnconfigure(i, weight=1, minsize=150)

    def calculate(self, target_entry):
        try:
            # Wert aus Zeile 2, Spalte 2 (Listeneinkaufspreis in €)
            listeneinkaufspreis = float(self.entries[0][2].get().replace("€", "").replace(",", "."))

            # Wert aus Zeile 2, Spalte 1 (Lieferantenrabatt in %)
            lieferantenrabatt_prozent = float(self.entries[1][1].get().replace("%", ""))
            lieferantenrabatt_wert = listeneinkaufspreis * (lieferantenrabatt_prozent / 100)

            # Wert aus Zeile 3, Spalte 1 (Lieferantenskonto in %)
            lieferantenskonto_prozent = float(self.entries[3][1].get().replace("%", ""))
            zieleinkaufspreis = listeneinkaufspreis - lieferantenrabatt_wert
            lieferantenskonto_wert = zieleinkaufspreis * (lieferantenskonto_prozent / 100)

            # Wert aus Zeile 6, Spalte 1 (Bezugskosten in €)
            bezugskosten = float(self.entries[5][1].get().replace("€", "").replace(",", "."))

            # Berechnungen
            bareinkaufspreis = zieleinkaufspreis - lieferantenskonto_wert
            handelskalkulation = bareinkaufspreis + bezugskosten
            bezugspreis = bareinkaufspreis + bezugskosten

            # Aktualisieren der Ergebnisfelder in der ersten Tabelle
            self.entries[2][2].delete(0, tk.END)
            self.entries[2][2].insert(0, f"{zieleinkaufspreis:.2f} €")

            self.entries[4][2].delete(0, tk.END)
            self.entries[4][2].insert(0, f"{bareinkaufspreis:.2f} €")

            self.entries[6][2].delete(0, tk.END)
            self.entries[6][2].insert(0, f"{handelskalkulation:.2f} €")

            self.entries[7][2].delete(0, tk.END)
            self.entries[7][2].insert(0, f"{bezugspreis:.2f} €")

            # Aktualisieren der Lieferantenrabatt- und Lieferantenskonto-Ergebnisfelder
            self.entries[1][2].delete(0, tk.END)
            self.entries[1][2].insert(0, f"{lieferantenrabatt_wert:.2f} €")

            self.entries[3][2].delete(0, tk.END)
            self.entries[3][2].insert(0, f"{lieferantenskonto_wert:.2f} €")

            # Einfügen des Bezugspreises in das Ziel-Eingabefeld in der zweiten Tabelle
            target_entry.delete(0, tk.END)
            target_entry.insert(0, f"{bezugspreis:.2f} €")

        except ValueError:
            pass  # Wenn eine ungültige Eingabe erfolgt, wird nichts berechnet

    def clear_entries(self):
        # Lösche alle Einträge aus der Tabelle
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    root.title("Handelskostenrechner")

    # Setze die Größe des Fensters
    window_width = 1200
    window_height = 800
    root.geometry(f"{window_width}x{window_height}")

    # Überschrift
    title_label = ttk.Label(root, text="Handelskostenrechner", font=("Helvetica", 20))
    title_label.pack(pady=(20, 40))

    # Header und Daten für die erste Tabelle
    headers1 = ["Bezugspreiskalkulation", "Zuschlagssätze in %", "Handelskalkulation in €"]
    table_data1 = [
        ["Listeneinkaufspreis", "", ""],
        ["- Lieferantenrabatt", "", ""],
        ["= Zieleinkaufspreis", "", ""],
        ["- Lieferantenskonto", "", ""],
        ["= Bareinkaufspreis", "", ""],
        ["+ Bezugskosten", "", ""],
        ["= Bezugspreis (BP)", "", ""]
    ]

    # Erste Tabelle
    table1 = InputTable(root, headers1, table_data1)
    table1.pack(pady=20, padx=20)

    # Referenz auf das entsprechende Eingabefeld in der zweiten Tabelle
    target_entry2 = table1.entries[6][2]

    # Frame für Buttons der ersten Tabelle
    button_frame1 = tk.Frame(root)
    button_frame1.pack()

    # Button zum Berechnen für die erste Tabelle
    calculate_button1 = ttk.Button(button_frame1, text="Berechnen", command=lambda: table1.calculate(target_entry2))
    calculate_button1.grid(row=0, column=0, sticky="nsew", padx=10)

    # Button zum Löschen für die erste Tabelle
    clear_button1 = ttk.Button(button_frame1, text="Löschen", command=table1.clear_entries)
    clear_button1.grid(row=0, column=1, sticky="nsew", padx=10)

    # Header und Daten für die zweite Tabelle
    headers2 = ["Verkaufspreiskalulation", "Zuschlagssätze in %", "Handelskalkulation in €"]
    table_data2 = [
        ["= Bezugspreis (BP)", "", ""],
        ["+ Handlungskosten", "", ""],
        ["= Selbstkosten", "", ""],
        ["+ Gewinn", "", ""],
        ["= Barverkaufspreis", "", ""],
        ["+ Kundenskonto", "", ""],
        ["= Zielverkaufspreis", "", ""],
        ["+ Kundenrabatt", "", ""],
        ["= Listenverkaufspreis (LVP)", "", ""],
    ]

    # Zweite Tabelle
    table2 = InputTable(root, headers2, table_data2)
    table2.pack(pady=20, padx=20)

    # Frame für Buttons der zweiten Tabelle
    button_frame2 = tk.Frame(root)
    button_frame2.pack()

    # Button zum Berechnen für die zweite Tabelle
    calculate_button2 = ttk.Button(button_frame2, text="Berechnen", command=table2.calculate)
    calculate_button2.grid(row=0, column=0, sticky="nsew", padx=10)

    # Button zum Löschen für die zweite Tabelle
    clear_button2 = ttk.Button(button_frame2, text="Löschen", command=table2.clear_entries)
    clear_button2.grid(row=0, column=1, sticky="nsew", padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
