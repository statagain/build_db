from pathlib import Path
from inspect import getmembers, isfunction
import sqlite3
import datasets

DB_PATH = Path('target') / 'statagain.db'

if __name__ == '__main__':
    # All functions exported from datasets whose name start with 'load_"
    # are considered dataset loaders and called to set up database.
    loaders = (func for name, func in getmembers(datasets, isfunction)
               if name.startswith('load_'))
    con = sqlite3.connect(DB_PATH)
    datasets.init_db(con)
    for loader in loaders:
        dataset = loader()
        dataset.to_sql(con)
        print(f"Loaded dataset ID: '{dataset.id}'.")
    con.close()
