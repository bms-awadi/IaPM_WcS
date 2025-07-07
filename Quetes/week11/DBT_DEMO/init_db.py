import pandas as pd
from sqlalchemy import create_engine

# Configuration de la base de données SQLite
db_url = "sqlite:///dbt_quest.db"
engine = create_engine(db_url)

# Vérification et création de la base de données (SQLite crée automatiquement le fichier si nécessaire)
print("Base de données SQLite configurée.")

# Liste des tables à importer
liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]

# Importation des fichiers CSV dans les tables SQLite
for table in liste_tables:
    csv_url = f"https://raw.githubusercontent.com/dsteddy/jaffle_shop_data/main/raw_{table}.csv"
    print(f"Téléchargement et importation de {table}...")
    df = pd.read_csv(csv_url)
    df.to_sql(f"raw_{table}", engine, if_exists="replace", index=False)
    print(f"Table {table} importée avec succès.")

print("Toutes les tables ont été importées.")