import pandas as pd
from sqlalchemy import create_engine


DB_USER = "datastore"
DB_PASSWORD = "datastore_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "datastore360"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("Connexion PostgreSQL réussie !")


df = pd.read_csv("../data/processed/dataset_rgpd.csv", skipinitialspace=True, quotechar='"')

df.columns = df.columns.str.strip()
print("Nombre de lignes :", len(df))
print("Nombre de colonnes :", len(df.columns))
print(df.columns.tolist())