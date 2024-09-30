import pandas as pd

# Carica il file CSV
file_path = 'datasets/dataset_statistiche_preprocessato.csv'  # Sostituisci con il percorso del tuo file CSV
df = pd.read_csv(file_path, sep=';')

# Controlla se la colonna 'name' esiste nel DataFrame
if 'name' not in df.columns:
    print("La colonna 'name' non esiste nel file CSV.")
else:
    # Conta le occorrenze di ciascun nome nella colonna 'name'
    nome_frequenze = df['name'].value_counts()

    # Ottieni i primi 3 nomi che si ripetono di più
    top_nomi = nome_frequenze.nlargest(3)

    # Stampa i risultati
    print("I primi 3 nomi che si ripetono di più sono:")
    for nome, frequenza in top_nomi.items():
        print(f"'{nome}' con {frequenza} occorrenze.")
