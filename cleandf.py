import pandas as pd


dfsk_db = pd.read_csv('sk_db.csv')


def cleaning():
    sk_db.drop('index',axis=1)

    