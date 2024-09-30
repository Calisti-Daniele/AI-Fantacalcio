import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
import joblib

# Carica il dataset preprocessato
df = pd.read_csv('datasets/dataset_statistiche_preprocessato.csv', sep=';')

# Crea un DataFrame per le statistiche da prevedere (media delle statistiche delle ultime 3 stagioni)
statistiche_precedenti = df.groupby('name').agg({
    'partite_valide': 'mean',
    'media_voto': 'mean',
    'goal_fatti': 'mean',
    'assist': 'mean',
    'ammonizioni': 'mean'
}).reset_index()

# Merge del DataFrame originale con le statistiche aggregate per ogni giocatore
df = pd.merge(df, statistiche_precedenti, on='name', suffixes=('', '_media'))

# Seleziona le colonne caratteristiche (statistiche storiche) e i target (valori da prevedere)
X = df[['partite_valide_media', 'media_voto_media', 'goal_fatti_media', 'assist_media', 'ammonizioni_media']]
y_targets = {
    'partite': df['partite_valide'],
    'media': df['media_voto'],
    'goal': df['goal_fatti'],
    'assist': df['assist'],
    'ammonizioni': df['ammonizioni']
}

# Standardizza le caratteristiche
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Crea un dizionario per i modelli e addestrali
models = {}
for target_name, y in y_targets.items():
    # Aggiungi caratteristiche polinomiali
    poly = PolynomialFeatures(degree=2)  # Puoi cambiare il grado a tuo piacimento
    X_poly = poly.fit_transform(X_scaled)

    X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    models[target_name] = model

    # Salva il modello
    joblib.dump(model, f'models/model_{target_name}.pkl')

# Salva il normalizzatore e il polinomial feature transformer
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(poly, 'models/poly_features.pkl')

print("Modelli e scaler salvati con successo.")
