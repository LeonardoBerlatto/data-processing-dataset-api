import pandas as pd


def load_dataset():
    print('Loading dataset...')
    df = pd.read_csv('./resources/data/sales.csv').set_index('Invoice ID')
    return df
