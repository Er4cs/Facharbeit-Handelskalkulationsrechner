import tkinter as tk


class HandelskostenGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Handelskostenkalkulation")

        # Labels und Eingabefelder für die Bezugspreiskalkulation
        self.label_bezugspreis = tk.Label(master, text="Bezugspreiskalkulation")
        self.label_bezugspreis.grid(row=0, column=0, columnspan=3)

        self.label_listeneinkaufspreis = tk.Label(master, text="Listeneinkaufspreis:")
        self.label_listeneinkaufspreis.grid(row=1, column=0)
        self.entry_listeneinkaufspreis = tk.Entry(master)
        self.entry_listeneinkaufspreis.grid(row=1, column=1, columnspan=2)
        self.entry_listeneinkaufspreis.config(bg="yellow")  # Markierung als Pflichtfeld

        self.label_liefer_rabatt = tk.Label(master, text="Liefer-Rabatt (%):")
        self.label_liefer_rabatt.grid(row=2, column=0)
        self.entry_liefer_rabatt = tk.Entry(master)
        self.entry_liefer_rabatt.grid(row=2, column=1, columnspan=2)
        self.entry_liefer_rabatt.config(bg="yellow")  # Markierung als Pflichtfeld

        self.label_liefer_skonto = tk.Label(master, text="Liefer-Skonto (%):")
        self.label_liefer_skonto.grid(row=3, column=0)
        self.entry_liefer_skonto = tk.Entry(master)
        self.entry_liefer_skonto.grid(row=3, column=1, columnspan=2)
        self.entry_liefer_skonto.config(bg="yellow")  # Markierung als Pflichtfeld

        # Label und Eingabefeld für die Bezugskosten
        self.label_bezugskosten = tk.Label(master, text="Bezugskosten (€):")
        self.label_bezugskosten.grid(row=4, column=0)
        self.entry_bezugskosten = tk.Entry(master)
        self.entry_bezugskosten.grid(row=4, column=1, columnspan=2)
        self.entry_bezugskosten.config(state='disabled')  # Deaktiviert, bis andere Werte eingegeben sind

        # Labels und Eingabefelder für die Verkaufspreiskalkulation
        self.label_verkaufspreis = tk.Label(master, text="Verkaufspreiskalkulation")
        self.label_verkaufspreis.grid(row=5, column=0, columnspan=3)

        self.label_handlungskosten = tk.Label(master, text="Handlungskosten (%):")
        self.label_handlungskosten.grid(row=6, column=0)
        self.entry_handlungskosten = tk.Entry(master)
        self.entry_handlungskosten.grid(row=6, column=1, columnspan=2)
        self.entry_handlungskosten.config(bg="yellow")  # Markierung als Pflichtfeld

        self.label_gewinn = tk.Label(master, text="Gewinn (%):")
        self.label_gewinn.grid(row=7, column=0)
        self.entry_gewinn = tk.Entry(master)
        self.entry_gewinn.grid(row=7, column=1, columnspan=2)
        self.entry_gewinn.config(bg="yellow")  # Markierung als Pflichtfeld

        self.label_kundenskonto = tk.Label(master, text="Kundenskonto (%):")
        self.label_kundenskonto.grid(row=8, column=0)
        self.entry_kundenskonto = tk.Entry(master)
        self.entry_kundenskonto.grid(row=8, column=1, columnspan=2)
        self.entry_kundenskonto.config(bg="yellow")  # Markierung als Pflichtfeld

        self.label_kundenrabatt = tk.Label(master, text="Kundenrabatt (%):")
        self.label_kundenrabatt.grid(row=9, column=0)
        self.entry_kundenrabatt = tk.Entry(master)
        self.entry_kundenrabatt.grid(row=9, column=1, columnspan=2)
        self.entry_kundenrabatt.config(bg="yellow")  # Markierung als Pflichtfeld

        # Button zur Berechnung
        self.button_berechnen = tk.Button(master, text="Kosten berechnen", command=self.berechne_kosten)
        self.button_berechnen.grid(row=10, column=0, columnspan=3)

        # Label für das Ergebnis
        self.label_ergebnis = tk.Label(master, text="")
        self.label_ergebnis.grid(row=11, column=0, columnspan=3)

        # Überwache Eingabefelder für Änderungen, um Bezugskosten zu aktualisieren
        self.entry_liefer_rabatt.bind("<KeyRelease>", self.aktualisiere_bezugskosten)
        self.entry_liefer_skonto.bind("<KeyRelease>", self.aktualisiere_bezugskosten)

    def aktualisiere_bezugskosten(self, event):
        # Aktualisiere Bezugskosten basierend auf Listeneinkaufspreis, Liefer-Rabatt und Liefer-Skonto
        listeneinkaufspreis = float(self.entry_listeneinkaufspreis.get())
        liefer_rabatt = float(self.entry_liefer_rabatt.get())
        liefer_skonto = float(self.entry_liefer_skonto.get())

        # Berechne die Bezugskosten
        bezugskosten = listeneinkaufspreis * (liefer_rabatt / 100) * (liefer_skonto / 100)
        # Aktualisiere das Eingabefeld für Bezugskosten
        self.entry_bezugskosten.config(state='normal')
        self.entry_bezugskosten.delete(0, tk.END)
        self.entry_bezugskosten.insert(0, str(bezugskosten))
        self.entry_bezugskosten.config(state='disabled')

    def berechne_kosten(self):
        # Überprüfen, ob alle Pflichtfelder ausgefüllt sind
        pflichtfelder = [
            self.entry_listeneinkaufspreis,
            self.entry_liefer_rabatt,
            self.entry_liefer_skonto,
            self.entry_handlungskosten,
            self.entry_gewinn,
            self.entry_kundenskonto,
            self.entry_kundenrabatt
        ]
        for field in pflichtfelder:
            if field.get() == "":
                field.config(bg="red")
                return
            else:
                field.config(bg="white")

        # Eingaben abrufen und in Float umwandeln
        listeneinkaufspreis = float(self.entry_listeneinkaufspreis.get())
        liefer_rabatt = float(self.entry_liefer_rabatt.get())
        liefer_skonto = float(self.entry_liefer_skonto.get())
        bezugskosten = float(self.entry_bezugskosten.get())
        handlungskosten = float(self.entry_handlungskosten.get())
        gewinn = float(self.entry_gewinn.get())
        kundenskonto = float(self.entry_kundenskonto.get())
        kundenrabatt = float(self.entry_kundenrabatt.get())

        # Bezugspreiskalkulation
        zieleinkaufspreis = listeneinkaufspreis * (1 - liefer_rabatt / 100)
        bareinkaufspreis = zieleinkaufspreis * (1 - liefer_skonto / 100)
        bezugspreis = bareinkaufspreis + bezugskosten

        # Verkaufspreiskalkulation
        selbstkosten = bezugspreis * (1 + handlungskosten / 100)
        barverkaufspreis = selbstkosten * (1 + gewinn / 100)
        zielverkaufspreis = barverkaufspreis * (1 + kundenskonto / 100)
        listenverkaufspreis = zielverkaufspreis * (1 - kundenrabatt / 100)

        # Ergebnis anzeigen
        ergebnis_text = f"Bezugspreis (BP): {bezugspreis:.2f} €\n"
        ergebnis_text += f"Listenverkaufspreis (LVP): {listenverkaufspreis:.2f} €"
        self.label_ergebnis.config(text=ergebnis_text)

def main():
    root = tk.Tk()
    app = HandelskostenGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
