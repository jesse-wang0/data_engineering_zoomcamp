import pandas as pd
from sqlalchemy import create_engine

username = "root"
password = "root"
host = "localhost"
port = "5432"
db_name = "ny_taxi"

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}')
engine.connect()
df_zones = pd.read_csv("taxi_zone_lookup.csv")
df_zones.to_sql(name="zones", con=engine, if_exists="replace")