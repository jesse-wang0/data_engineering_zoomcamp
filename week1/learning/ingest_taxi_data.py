import argparse
import pandas as pd
import os
from sqlalchemy import create_engine

def main(params):
    engine = create_engine(f'postgresql://{params.username}:{params.password}@{params.host}:{params.port}/{params.db_name}')
    engine.connect()

    download_name = "taxi_data.csv.gz"
    os.system(f"wget -O {download_name} {params.url}")
    os.system(f"gzip -d {download_name}")

    csv_name = "taxi_data.csv"
    df_taxi = pd.read_csv(csv_name, nrows=100)
    df_taxi['tpep_pickup_datetime'] = pd.to_datetime(df_taxi['tpep_pickup_datetime'])
    df_taxi['tpep_dropoff_datetime'] = pd.to_datetime(df_taxi['tpep_dropoff_datetime'])

    df_taxi.head(0).to_sql(name=params.table_name, con=engine, if_exists='replace')

    for chunk in pd.read_csv(csv_name, chunksize=100000):
        print("Start inserting chunk")
        chunk['tpep_pickup_datetime'] = pd.to_datetime(chunk['tpep_pickup_datetime'])
        chunk['tpep_dropoff_datetime'] = pd.to_datetime(chunk['tpep_dropoff_datetime'])
        chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
        print("Finish inserting chunk")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='TaxiDataIngest',
                    description='Ingests data from a given link into chosen database'
                    )

    parser.add_argument('-U', '--username', help='Username for postgres')
    parser.add_argument('-P', '--password', help='Password for postgres')
    parser.add_argument('-H', '--host', help='Host for postgres')
    parser.add_argument('-p', '--port', help='Port for postgres')
    parser.add_argument('-d', '--db_name', help='Name of database in postgres')
    parser.add_argument('-t', '--table_name', help='Name of table in postgres')
    parser.add_argument('-u', '--url', help='URL of CSV file to download')
    args = parser.parse_args()

    main(args)