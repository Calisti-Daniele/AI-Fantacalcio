import pandas as pd


def migliori_giocatori(ruolo_df, numero_giocatori, stat='media_voto'):
    """
    Seleziona i migliori giocatori per ciascun ruolo.

    :param ruolo_df: DataFrame con i giocatori di un ruolo specifico.
    :param numero_giocatori: Numero di giocatori da selezionare.
    :param stat: Statistica sulla quale basare la selezione.
    :return: DataFrame con i migliori giocatori selezionati.
    """
    return ruolo_df.nlargest(numero_giocatori, stat)


def filtra_giocatori_per_ruolo(risultati_df):
    """
    Filtra i giocatori per ciascun ruolo e seleziona i migliori.

    :param risultati_df: DataFrame contenente tutte le previsioni dei giocatori.
    :return: Migliori giocatori per ciascun ruolo.
    """
    migliori_portieri = migliori_giocatori(risultati_df[risultati_df['role'] == 'P'], 3)
    migliori_difensori = migliori_giocatori(risultati_df[risultati_df['role'] == 'D'], 8)
    migliori_centrocampisti = migliori_giocatori(risultati_df[risultati_df['role'] == 'C'], 8)
    migliori_attaccanti = migliori_giocatori(risultati_df[risultati_df['role'] == 'A'], 6)

    return migliori_portieri, migliori_difensori, migliori_centrocampisti, migliori_attaccanti
