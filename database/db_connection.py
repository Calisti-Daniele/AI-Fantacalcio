# db_connection.py

import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self, host='localhost', user='root', password='', database='fanta_ai'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def create_connection(self):
        """Crea una connessione al database MySQL."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connessione al database riuscita.")
        except Error as e:
            print(f"Errore durante la connessione al database: {e}")
            self.connection = None

    def close_connection(self):
        """Chiude la connessione al database."""
        if self.connection.is_connected():
            self.connection.close()
            print("Connessione al database chiusa.")

    def get_connection(self):
        """Restituisce la connessione al database."""
        return self.connection
