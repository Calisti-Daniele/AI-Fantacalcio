import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
import joblib

# Carica il dataset preprocessato
df = pd.read_csv('datasets/dataset_statistiche_preprocessato.csv', sep=';')

# Crea un DataFrame per le statistiche da prevedere (media delle statistiche delle ultime 3 stagioni)
statistiche_precedenti = df.groupby('name').agg({
    'partite_valide': 'mean',
    'media_voto': 'mean',
    'goal_fatti': 'mean',
    'assist': 'mean',
    'ammonizioni': 'mean',
    'espulsioni': 'mean',
    'goal_subiti': 'mean'
}).reset_index()

# Merge del DataFrame originale con le statistiche aggregate per ogni giocatore
df = pd.merge(df, statistiche_precedenti, on='name', suffixes=('', '_media'))

# Seleziona le colonne caratteristiche (statistiche storiche) e i target (valori da prevedere)
X = df[['partite_valide_media', 'media_voto_media', 'goal_fatti_media', 'assist_media', 'ammonizioni_media',
        'espulsioni_media']]
y_targets = {
    'partite': df['partite_valide'],
    'media': df['media_voto'],
    'goal': df['goal_fatti'],
    'assist': df['assist'],
    'espulsioni': df['espulsioni'],
    'ammonizioni': df['ammonizioni']
}

# Crea un dizionario per i modelli
models = {}
for target_name, y in y_targets.items():
    # Definisci una pipeline per la standardizzazione, polinomial features e il modello regolarizzato
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('poly', PolynomialFeatures(degree=3)),
        ('model', Ridge(alpha=1.0))  # Modello Ridge con regolarizzazione L2
    ])

    # Cross-validation per valutare il modello
    scores = cross_val_score(pipeline, X, y, cv=5, scoring='neg_mean_squared_error')
    print(f"Cross-validation MSE per {target_name}: {-scores.mean():.4f}")

    # Addestra il modello sull'intero dataset
    pipeline.fit(X, y)

    # Salva il modello con tutta la pipeline
    joblib.dump(pipeline, f'models/model_{target_name}.pkl')
    models[target_name] = pipeline

print("Tutti i modelli e le pipeline sono stati salvati con successo.")
