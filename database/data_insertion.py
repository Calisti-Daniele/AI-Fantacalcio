# data_insertion.py

from database.db_connection import DatabaseConnection
from database.bean.previsione_miglior_team import PrevisioneMigliorTeam


class DataInsertion:
    def __init__(self):
        self.db = DatabaseConnection(host='localhost', user='root', password='', database='fanta_ai')
        self.db.create_connection()

    def clear_previsione_miglior_team(self):
        """Svuota la tabella previsione_miglior_team nel database."""
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("TRUNCATE TABLE previsione_miglior_team")  # O usa DELETE se preferisci
            connection.commit()
            print("Tabella previsione_miglior_team svuotata con successo.")
        except Exception as e:
            print(f"Errore durante lo svuotamento della tabella: {e}")
        finally:
            cursor.close()

    def insert_previsione_miglior_team(self, previsione: PrevisioneMigliorTeam):
        """Inserisce una nuova previsione nel database."""
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor()
            sql = """INSERT INTO previsione_miglior_team (nome, ruolo, media_voto, squadra, assist, goal_fatti, ammonizioni, espulsioni) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                previsione.nome,
                previsione.ruolo,
                previsione.media_voto,
                previsione.squadra,
                previsione.assist,
                previsione.goal_fatti,
                previsione.ammonizioni,
                previsione.espulsioni
            )
            cursor.execute(sql, values)
            connection.commit()
            print("Previsione inserita con successo.")
        except Exception as e:
            print(f"Errore durante l'inserimento della previsione: {e}")
        finally:
            cursor.close()


    def insert_previsione_giocatore(self, previsione: PrevisioneMigliorTeam):
        """Inserisce una nuova previsione nel database."""
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor()
            sql = """INSERT INTO previsione_giocatori (nome, ruolo, media_voto, squadra, assist, goal_fatti, ammonizioni, espulsioni) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                previsione.nome,
                previsione.ruolo,
                previsione.media_voto,
                previsione.squadra,
                previsione.assist,
                previsione.goal_fatti,
                previsione.ammonizioni,
                previsione.espulsioni
            )
            cursor.execute(sql, values)
            connection.commit()
            print("Previsione inserita con successo.")
        except Exception as e:
            print(f"Errore durante l'inserimento della previsione: {e}")
        finally:
            cursor.close()

    def close(self):
        """Chiude la connessione al database."""
        self.db.close_connection()
