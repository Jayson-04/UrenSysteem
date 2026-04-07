import csv
import os
from datetime import datetime

BESTANDSNAAM = "urenregistratie.csv"

def initialiseer_csv():
    """Maak CSV-bestand aan met headers als het nog niet bestaat."""
    if not os.path.exists(BESTANDSNAAM):
        with open(BESTANDSNAAM, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["datum", "starttijd", "eindtijd", "totaal_uren", "omschrijving"])
        print(f"Nieuw CSV-bestand aangemaakt: {BESTANDSNAAM}")

def vraag_invoer():
    """Vraag de gebruiker om gegevens in te voeren."""
    print("\n--- Nieuwe urenregistratie ---")

    datum = input("Datum (YYYY-MM-DD): ")
    starttijd = input("Starttijd (HH:MM): ")
    eindtijd = input("Eindtijd (HH:MM): ")
    omschrijving = input("Omschrijving van het werk: ")

    tijd_start = datetime.strptime(f"{datum} {starttijd}", "%Y-%m-%d %H:%M")
    tijd_eind = datetime.strptime(f"{datum} {eindtijd}", "%Y-%m-%d %H:%M")
    totaal_uren = round((tijd_eind - tijd_start).seconds / 3600, 2)

    return [datum, starttijd, eindtijd, totaal_uren, omschrijving]

def schrijf_naar_csv(regel):
    """Schrijf een nieuwe regel naar het CSV-bestand."""
    with open(BESTANDSNAAM, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(regel)
    print("\n✔ Gegevens opgeslagen!")

def main():
    initialiseer_csv()

    while True:
        gegevens = vraag_invoer()
        schrijf_naar_csv(gegevens)

        verder = input("\nNog een registratie toevoegen? (j/n): ").lower()
        if verder != "j":
            print("\nProgramma afgesloten. CSV-bestand bijgewerkt.")
            break

if __name__ == "__main__":
    main()
