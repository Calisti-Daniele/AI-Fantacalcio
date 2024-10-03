import pandas as pd
from data_preprocessing import carica_dataset_preprocessato
from modello_previsione import prevedi_statistiche
from analisi_giocatori import filtra_giocatori_per_ruolo
from database.data_insertion import DataInsertion
from database.bean.previsione_miglior_team import PrevisioneMigliorTeam


def ottieni_previsioni_giocatore(nome_giocatore, risultati_df):
    """
    Cerca un giocatore per nome e restituisce le sue previsioni.

    :param nome_giocatore: Nome del giocatore da cercare.
    :param risultati_df: DataFrame contenente tutte le previsioni dei giocatori.
    :return: Previsioni per il giocatore, o messaggio di errore se non trovato.
    """
    giocatore = risultati_df[risultati_df['name'].str.contains(nome_giocatore, case=False)]
    if giocatore.empty:
        return f"Nessun giocatore trovato con il nome: {nome_giocatore}"
    else:
        return giocatore[['name', 'media_voto', 'team', 'assist', 'goal_fatti', 'ammonizioni', 'espulsioni']]


# Carica e prepara il dataset
df_preprocessato, df_preprocessato_tutti_giocatori = carica_dataset_preprocessato(
    '../datasets/dataset_statistiche_preprocessato.csv',
    '../datasets/dataset_lista_giocatori_stagione_odierna.csv')

# Calcola le statistiche per tutti i giocatori
migliori_giocatori = prevedi_statistiche(df_preprocessato)

tutti_giocatori = prevedi_statistiche(df_preprocessato_tutti_giocatori)

# Converte i risultati in un DataFrame
risultati_df_migliori = pd.DataFrame(migliori_giocatori)
risultati_df_totali = pd.DataFrame(tutti_giocatori)

# Rimuovi i duplicati basati sul nome del giocatore
risultati_df_migliori = risultati_df_migliori.drop_duplicates(subset='name')
risultati_df_tutti = risultati_df_totali.drop_duplicates(subset='name')

# Seleziona i migliori giocatori per ciascun ruolo
migliori_portieri, migliori_difensori, migliori_centrocampisti, migliori_attaccanti = filtra_giocatori_per_ruolo(
    risultati_df_migliori)

# Inizializza il modulo di inserimento dati
inserter = DataInsertion()


# Funzione per inserire i migliori giocatori nel database
def inserisci_giocatori(giocatori_df, ruolo):
    for index, row in giocatori_df.iterrows():
        previsione = PrevisioneMigliorTeam(
            nome=row['name'],
            ruolo=ruolo,
            media_voto=row['media_voto'],
            squadra=row['team'],
            assist=row.get('assist', 0),
            goal_fatti=row.get('goal_fatti', 0),
            ammonizioni=row['ammonizioni'],
            espulsioni=row['espulsioni']
        )
        inserter.insert_previsione_miglior_team(previsione)

def inserisci_giocatore(giocatori_df):
    for index, row in giocatori_df.iterrows():
        previsione = PrevisioneMigliorTeam(
            nome=row['name'],
            ruolo=row['role'],
            media_voto=row['media_voto'],
            squadra=row['team'],
            assist=row.get('assist', 0),
            goal_fatti=row.get('goal_fatti', 0),
            ammonizioni=row['ammonizioni'],
            espulsioni=row['espulsioni']
        )
        inserter.insert_previsione_giocatore(previsione)

inserter.clear_previsione_miglior_team()

# Inserisci i migliori giocatori nel database
inserisci_giocatori(migliori_portieri, 'P')
inserisci_giocatori(migliori_difensori, 'D')
inserisci_giocatori(migliori_centrocampisti, 'C')
inserisci_giocatori(migliori_attaccanti, 'A')

inserisci_giocatore(risultati_df_tutti)

# Chiudi la connessione dopo l'uso
inserter.close()

print("Giocatori inseriti con successo nel database.")
