from pathlib import Path
import pandas as pd
from . import __file__ as package_top
from .sql import CREATE_DATASET_DDL, CREATE_FEATURE_DDL


def get_working_dir():
    """Returns full path to the datasets directory"""
    return Path(package_top).parent


class Dataset:
    """Dataset data, metadata and database load code.

    Holds dataset info, feature descriptions, and data ready to be flushed
    to sqlite database. Returned by load_... dataset-specific function.
    """
    def __init__(
            self,
            id_: str,
            name: str,
            title: str,
            url: str,
            attribution: str,
            description: str,
            features: dict,
            data=None):
        self.id = id_
        self.name = name
        self.title = title
        self.url = url
        self.attribution = attribution
        self.description = description
        self.features = features
        self.data = data

    def _delete_from_sql(self, con):
        con.execute('DELETE FROM feature WHERE dataset_id=(?)', (self.id,))
        con.execute('DELETE FROM dataset WHERE id=(?)', (self.id,))
        con.execute(f'DROP TABLE IF EXISTS {self.id}')

    def to_sql(self, con):
        """Flushes metadata and data to the database."""
        dataset_dml = 'INSERT INTO dataset VALUES (?, ?, ?, ?, ?, ?)'
        dataset_values = (self.id, self.name, self.title,
                          self.url, self.attribution, self.description)
        feature_dml = 'INSERT INTO feature VALUES (?, ?, ?)'
        feature_values = [(self.id, name, description)
                          for name, description in
                          self.features.items()]
        self._delete_from_sql(con)
        con.execute(dataset_dml, dataset_values)
        con.executemany(feature_dml, feature_values)
        con.commit()
        if isinstance(self.data, pd.DataFrame):
            self.data.to_sql(self.name, con, index=False)


def init_db(con):
    """Creates database schema."""
    con.execute(CREATE_DATASET_DDL)
    con.execute(CREATE_FEATURE_DDL)
