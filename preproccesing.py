import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# Carica il dataset
df = pd.read_csv('dataset_statistiche.csv', sep=';')

# Step 1: Gestione dei valori mancanti
# Converti 'autogoal' in numerico e riempi i valori mancanti con 0
df['autogoal'] = pd.to_numeric(df['autogoal'], errors='coerce').fillna(0)

# Riempi i valori mancanti in 'stagione' con 'Unknown'
df['stagione'] = df['stagione'].fillna('Unknown')

# Step 2: Conversione di 'espulsioni' in numerico
df['espulsioni'] = pd.to_numeric(df['espulsioni'], errors='coerce').fillna(0)

# Step 3: Normalizzazione dei dati numerici
numerical_cols = ['media_voto', 'fanta_media', 'goal_fatti', 'goal_subiti',
                  'rigori_parati', 'rigori_totali', 'rigori_segnati', 'rigori_sbagliati',
                  'assist', 'ammonizioni', 'espulsioni', 'autogoal']

# Inizializza lo scaler
scaler = MinMaxScaler()

# Applica la normalizzazione
#df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Mostra il dataset preprocessato
print(df.tail())
