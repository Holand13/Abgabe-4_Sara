# Leistungskurve II

## Projektbeschreibung

Dieses Projekt enthält ein Modul zur Berechnung und Darstellung einer Leistungskurve basierend auf Leistungsdaten in Watt aus einer CSV-Datei (`activity.csv`). Das Modul umfasst Funktionen zur Berechnung der maximalen Dauer, für die verschiedene Leistungsniveaus aufrechterhalten werden können, sowie zur Erstellung eines Plots der Leistungskurve.

## Funktionen

### `make_plot(df)`

Diese Funktion erstellt ein Liniendiagramm der Leistung pro Zeit.

- **Eingabe:** DataFrame `df` mit den Spalten "Time" und "PowerOriginal"
- **Ausgabe:** Plotly-Figur

### `calculate_duration(df, power_level)`

Diese Funktion berechnet die maximale Dauer, für die ein bestimmtes Leistungsniveau überschritten wird.

- **Eingabe:** 
  - DataFrame `df` mit den Spalten "Time" und "PowerOriginal"
  - `power_level`: Leistungsniveau in Watt
- **Ausgabe:** Maximale Dauer in Sekunden

### `calc_maxdurationpower(df)`

Diese Funktion berechnet für jedes Leistungsniveau die maximale Dauer und sortiert die Ergebnisse.

- **Eingabe:** DataFrame `df` mit den Spalten "Time" und "PowerOriginal"
- **Ausgabe:** 
  - `unsortdata`: Unsortierter DataFrame mit den Spalten "PowerOriginal" und "MaxDuration"
  - `df_sorted`: Nach "MaxDuration" sortierter DataFrame

## Voraussetzungen

Erstellen Sie eine virtuelle Umgebung und installieren Sie die benötigten Bibliotheken aus der `requirements.txt`:


### Verwendung

Stellen Sie sicher, dass die Datei `activity.csv` im gleichen Verzeichnis wie `functions.py` und `main.py` vorhanden ist.
Führen Sie das Skript `main.py` mit dem Befehl `streamlit run main.py` aus, um die Analyse durchzuführen und die Plots zu erstellen.


```bash
python -m venv venv
source `venv\Scripts\activate`
pip install -r requirements.txt