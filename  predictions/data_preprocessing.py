import pandas as pd
import numpy as np

def carica_dataset_preprocessato(preprocessato_path, oggi_path):
    """
    Carica e preprocessa i dataset dei giocatori.

    :param preprocessato_path: Percorso al file CSV con i dati preprocessati.
    :param oggi_path: Percorso al file CSV con i dati della stagione odierna.
    :return: DataFrame filtrato e aggiornato con i dati più recenti dei giocatori.
    """
    # Carica il dataset di statistiche
    df_preprocessato = pd.read_csv(preprocessato_path, sep=';')

    # Carica il dataset "oggi_dataset"
    oggi_dataset = pd.read_csv(oggi_path, sep=';')

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
    df_preprocessato_tutti_giocatori = df_preprocessato
    df_preprocessato = df_preprocessato[df_preprocessato['migliore'] == 1]

    return df_preprocessato, df_preprocessato_tutti_giocatori
