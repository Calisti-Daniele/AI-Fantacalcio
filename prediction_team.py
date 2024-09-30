import joblib
import numpy as np
import pandas as pd

# Carica i modelli e lo scaler
model_partite = joblib.load('models/model_partite.pkl')
model_media = joblib.load('models/model_media.pkl')
model_goal = joblib.load('models/model_goal.pkl')
model_assist = joblib.load('models/model_assist.pkl')
model_ammonizioni = joblib.load('models/model_ammonizioni.pkl')
scaler = joblib.load('models/scaler.pkl')
poly = joblib.load('models/poly_features.pkl')  # Carica il trasformatore polinomiale

# Carica il dataset di statistiche
df_preprocessato = pd.read_csv('datasets/dataset_statistiche_preprocessato.csv', sep=';')

# Carica il dataset "oggi_dataset"
oggi_dataset = pd.read_csv('datasets/dataset_lista_giocatori_stagione_odierna.csv', sep=';')

# Filtra il DataFrame per mantenere solo i giocatori presenti in "oggi_dataset"
df_preprocessato = df_preprocessato[df_preprocessato['name'].isin(oggi_dataset['name'])]

# Aggiorna i team dei giocatori nel DataFrame preprocessato
df_preprocessato = df_preprocessato.merge(oggi_dataset[['name', 'team']], on='name', how='left',
                                          suffixes=('', '_nuovo'))

# Aggiorna la colonna 'team' se il team è diverso
df_preprocessato['team'] = np.where(df_preprocessato['team'] != df_preprocessato['team_nuovo'],
                                    df_preprocessato['team_nuovo'], df_preprocessato['team'])

# Rimuovi la colonna temporanea 'team_nuovo'
df_preprocessato.drop(columns=['team_nuovo'], inplace=True)

# Filtra il DataFrame per considerare solo le righe con 'migliore' uguale a 1
df_preprocessato = df_preprocessato[df_preprocessato['migliore'] == 1]


# Funzione per prevedere le statistiche di tutti i giocatori
def prevedi_statistiche(df):
    results = []
    for index, row in df.iterrows():
        player_stats = {
            'partite_valide_media': row['partite_valide'],
            'media_voto_media': row['media_voto'],
            'goal_fatti_media': row['goal_fatti'],
            'assist_media': row['assist'],
            'ammonizioni_media': row['ammonizioni']
        }

        # Prepara i dati in un array 2D
        X_new = np.array([[player_stats['partite_valide_media'],
                           player_stats['media_voto_media'],
                           player_stats['goal_fatti_media'],
                           player_stats['assist_media'],
                           player_stats['ammonizioni_media']]])

        # Standardizza le caratteristiche
        X_new_scaled = scaler.transform(X_new)

        # Aggiungi caratteristiche polinomiali
        X_new_poly = poly.transform(X_new_scaled)

        # Esegui le previsioni
        previsioni = {
            'name': row['name'],
            'partite_valide': int(model_partite.predict(X_new_poly)[0]),
            'media_voto': model_media.predict(X_new_poly)[0],
            'goal_fatti': model_goal.predict(X_new_poly)[0],
            'assist': model_assist.predict(X_new_poly)[0],
            'ammonizioni': model_ammonizioni.predict(X_new_poly)[0],
            'role': row['role'],  # Assicurati che ci sia una colonna 'role' nel tuo DataFrame
            'team': row['team']
        }

        results.append(previsioni)

    return results


# Calcola le statistiche per tutti i giocatori
tutti_giocatori = prevedi_statistiche(df_preprocessato)

# Converte i risultati in un DataFrame
risultati_df = pd.DataFrame(tutti_giocatori)

# Rimuovi i duplicati basati sul nome del giocatore
risultati_df = risultati_df.drop_duplicates(subset='name')


# Funzione per ottenere i migliori giocatori per ciascun ruolo
def migliori_giocatori(ruolo_df, numero_giocatori, stat='media_voto'):
    return ruolo_df.nlargest(numero_giocatori, stat)


# Seleziona i migliori giocatori per ciascun ruolo
migliori_portieri = migliori_giocatori(risultati_df[risultati_df['role'] == 'P'], 3)
migliori_difensori = migliori_giocatori(risultati_df[risultati_df['role'] == 'D'], 8)
migliori_centrocampisti = migliori_giocatori(risultati_df[risultati_df['role'] == 'C'], 8)
migliori_attaccanti = migliori_giocatori(risultati_df[risultati_df['role'] == 'A'], 6)

# Stampa i risultati
print("Migliori portieri:")
print(migliori_portieri[['name', 'media_voto', 'team']])

print("\nMigliori difensori:")
print(migliori_difensori[['name', 'media_voto', 'team']])

print("\nMigliori centrocampisti:")
print(migliori_centrocampisti[['name', 'media_voto', 'team']])

print("\nMigliori attaccanti:")
print(migliori_attaccanti[['name', 'media_voto', 'team']])
