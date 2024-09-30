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
df = pd.read_csv('datasets/dataset_statistiche_preprocessato.csv', sep=';')

# Funzione per prevedere le statistiche di un giocatore basato sul suo nome
def prevedi_statistiche_per_giocatore(nome_giocatore):
    # Filtra il dataframe per il giocatore specifico
    player_data = df[df['name'] == nome_giocatore]

    # Controlla se il giocatore esiste nel dataset
    if player_data.empty:
        return f"Giocatore '{nome_giocatore}' non trovato."

    # Calcola le statistiche medie per il giocatore
    player_stats = {
        'partite_valide_media': player_data['partite_valide'].mean(),
        'media_voto_media': player_data['media_voto'].mean(),
        'goal_fatti_media': player_data['goal_fatti'].mean(),
        'assist_media': player_data['assist'].mean(),
        'ammonizioni_media': player_data['ammonizioni'].mean()
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
    partite_predette = int(model_partite.predict(X_new_poly)[0])  # Converti in intero
    media_predetta = model_media.predict(X_new_poly)[0]
    goal_predetti = model_goal.predict(X_new_poly)[0]
    assist_predetti = model_assist.predict(X_new_poly)[0]
    ammonizioni_predette = model_ammonizioni.predict(X_new_poly)[0]

    # Ritorna i risultati
    return {
        'partite_valide': partite_predette,
        'media_voto': media_predetta,
        'goal_fatti': goal_predetti,
        'assist': assist_predetti,
        'ammonizioni': ammonizioni_predette
    }

# Esempio di utilizzo
nome_giocatore = 'Gatti'  # Sostituisci con il nome del giocatore
previsioni = prevedi_statistiche_per_giocatore(nome_giocatore)

# Stampa i risultati delle previsioni
print(f"Previsioni per il giocatore '{nome_giocatore}':")
print(previsioni)
