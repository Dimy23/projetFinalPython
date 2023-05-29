import sqlite3
from album import Album

class Database:
    def __init__(self, db_name):
        self.connexion = sqlite3.connect(db_name)
        self.cursor = self.connexion.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS albums (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT,
                nomAuteur TEXT,
                annee INTEGER,
                prenomAuteur TEXT,
                nbreChansons INTEGER
                
            )
        ''')
        self.connexion.commit()

    def ajouter_album(self, titre, nomAuteur, annee, prenomAuteur, nbreChansons):
            self.cursor.execute("""
                 INSERT INTO albums (titre, nomAuteur, annee, prenomAuteur, nbreChansons) VALUES (?, ?, ?, ?, ?)
            """, (titre, nomAuteur, annee, prenomAuteur, nbreChansons))
            self.connexion.commit()
            
    def recuperer_albums(self):
        self.cursor.execute('''
            SELECT * FROM albums
        ''')
        rows = self.cursor.fetchall()
        albums = []
        for row in rows:
            album = Album(*row)  # Constructing the Album object
            albums.append(album)
        return albums

    def fermer_connexion(self):
        self.connexion.close()
