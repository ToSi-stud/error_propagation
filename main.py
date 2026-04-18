import math
from fehlerfortpflanzung import fehlerfortpflanzung


def main():
    dataset = []
    anzahl = int(input("Geben Sie die Anzahl der Datensätze ein: "))
    werte = int(input("Geben Sie die Anzahl der Werte pro Datensatz ein: "))
    for i in range(anzahl):
        datensatz = []
        for j in range(werte):
            wert = float(input(f"Geben Sie den Wert {j + 1} für Datensatz {i + 1} ein: "))
            datensatz.append(wert)
        dataset.append(datensatz)

    try:
        ergebnisse = fehlerfortpflanzung(dataset)
    except Exception as e:
        print("Fehler beim Ausführen von fehlerfortpflanzung:", e)
        return

    # Sicherstellen, dass erwartete Keys vorhanden sind
    try:
        sys_err = ergebnisse['Gesamtfehler_systematisch']
        rand_err = ergebnisse['Gesamtfehler_zufällig']
        R = ergebnisse['R']
    except Exception as e:
        print("Erwartete Ausgabefelder fehlen in den Ergebnissen:", e)
        return

    print("Gesamtfehler systematisch:", sys_err, "\nGesamtfehler zufällig:", rand_err, "\nR:", R)
    print("R=(", R, "±", sys_err, ") Ω")
    print("R=(", R, "±", rand_err, ") Ω")
    print("\n\n---------------------------------------- Vollständige Ergebnisse ----------------------------------------")
    for key, value in ergebnisse.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
