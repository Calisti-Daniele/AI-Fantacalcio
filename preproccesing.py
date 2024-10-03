import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Carica il dataset da un file CSV
df = pd.read_csv('datasets/dataset_statistiche.csv', sep=';')

# Step 1: Gestione dei valori mancanti
df['autogoal'] = pd.to_numeric(df['autogoal'].replace(',', '.'), errors='coerce').fillna(0)
df['stagione'] = df['stagione'].fillna('Unknown')
df['espulsioni'] = pd.to_numeric(df['espulsioni'].replace(',', '.'), errors='coerce').fillna(0)

normalize_decimals = ['media_voto', 'fanta_media']
df[normalize_decimals] = df[normalize_decimals].replace(',', '.', regex=True)

# Step 2: Conversione delle colonne numeriche in valori numerici
numerical_cols = ['media_voto', 'fanta_media', 'goal_fatti', 'goal_subiti',
                  'rigori_parati', 'rigori_totali', 'rigori_segnati', 'rigori_sbagliati',
                  'assist', 'ammonizioni', 'espulsioni', 'autogoal']
df[numerical_cols] = df[numerical_cols].apply(pd.to_numeric, errors='coerce')

# Step 3: Aggiungi una colonna 'migliore' che etichetta i migliori giocatori
df['migliore'] = 0
df.loc[(df['role'] == 'P') & (df['fanta_media'] >= 5) & (df['partite_valide'] >= 30) & (df['goal_subiti'] <= 47) & (df['ammonizioni'] <= 2), 'migliore'] = 1
df.loc[(df['role'] == 'D') & (df['fanta_media'] >= 5.5) & (df['partite_valide'] >= 16) & (df['goal_fatti'] >= 2) & (df['assist'] >= 2) & (df['ammonizioni'] <= 6), 'migliore'] = 1
df.loc[(df['role'] != 'P') & (df['role'] != 'D') & (df['fanta_media'] >= 5.5) & (df['partite_valide'] >= 16) & (df['goal_fatti'] >= 4) & (df['assist'] >= 2) & (df['ammonizioni'] <= 3), 'migliore'] = 1

# Step 4: Identificare la stagione più recente
# Manteniamo la colonna 'stagione' come stringa
# Estrai l'anno finale dalla stagione e convertiamolo in datetime
df['anno_finale'] = df['stagione'].str.split('-').str[1].astype(int)

# Identifica la stagione più recente
stagione_recente = df['anno_finale'].max()

# Step 5: Filtra i giocatori che compaiono nella stagione più recente
# Ottieni tutti i giocatori presenti nella stagione più recente
giocatori_stagione_recente = df[df['anno_finale'] == stagione_recente]['name'].unique()

# Step 6: Mantieni anche i dati per questi giocatori nelle stagioni precedenti
# Filtra il dataset per mantenere solo i giocatori presenti nella stagione recente o nelle stagioni precedenti
df = df[df['name'].isin(giocatori_stagione_recente)]


# Step 8: Salvataggio del DataFrame preprocessato come CSV
df.to_csv('dataset_statistiche_preprocessato.csv', sep=';', index=False)

