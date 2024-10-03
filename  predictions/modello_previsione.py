import numpy as np
import joblib
import pandas as pd

# Carica i modelli (le pipeline che includono lo scaler e il trasformatore polinomiale)
model_partite = joblib.load('../models/model_partite.pkl')
model_media = joblib.load('../models/model_media.pkl')
model_goal = joblib.load('../models/model_goal.pkl')
model_assist = joblib.load('../models/model_assist.pkl')
model_espulsioni = joblib.load('../models/model_espulsioni.pkl')
model_ammonizioni = joblib.load('../models/model_ammonizioni.pkl')


def prevedi_statistiche(df):
    """
    Funzione per prevedere le statistiche di tutti i giocatori.

    :param df: DataFrame contenente le statistiche preprocessate dei giocatori.
    :return: Lista di dizionari con le previsioni per ogni giocatore.
    """
    results = []

    for index, row in df.iterrows():
        # Prepara le features per la previsione
        X_new = np.array([[row['partite_valide'], row['media_voto'], row['goal_fatti'],
                           row['assist'], row['ammonizioni'], row['espulsioni']]])

        # Esegui le previsioni con i modelli caricati (pipeline)
        previsioni = {
            'name': row['name'],
            'role': row['role'],
            'team': row['team'],
            'partite_valide': int(model_partite.predict(X_new)[0]),
            'media_voto': model_media.predict(X_new)[0],
            'goal_fatti': model_goal.predict(X_new)[0],
            'assist': model_assist.predict(X_new)[0],
            'ammonizioni': model_ammonizioni.predict(X_new)[0],
            'espulsioni': model_espulsioni.predict(X_new)[0]
        }

        results.append(previsioni)

    return results


# Esempio di utilizzo
df = pd.read_csv('../datasets/dataset_statistiche_preprocessato.csv', sep=';')
previsioni = prevedi_statistiche(df)

# Stampa le previsioni per verifica
for p in previsioni:
    print(p)
