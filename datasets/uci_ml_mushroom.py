import pandas as pd
from .core import get_working_dir, Dataset


dataset_info = {
    'id_': 'UCI_ML_mushroom',
    'name': 'mushrooms',
    'title': 'Mushroom Data Set',
    'url': 'https://archive.ics.uci.edu/ml/datasets/mushroom',
    'attribution':
        'G. H. Lincoff (Pres.), New York: Alfred A. Knopf, '
        'Jeff Schlimmer (Jeffrey.Schlimmer@a.gp.cs.cmu.edu), David W. Aha',
    'description':
        'From Audobon Society Field Guide; '
        'mushrooms described in terms of physical characteristics; '
        'classification: poisonous or edible'
}


def load_mushrooms():
    dataset_id = dataset_info['id_']
    dataset_dir = get_working_dir() / f'{dataset_id}'
    desc_file = dataset_dir / 'agaricus-lepiota.names'
    data_file = dataset_dir / 'agaricus-lepiota.data'
    # Get features from description
    with open(desc_file, 'r', encoding='UTF-8') as f:
        dataset_desc = f.read()
    dataset_features = {'class': 'edible=e,poisonous=p'}
    key, value = None, None
    in_decode_area = False
    for line in dataset_desc.splitlines():
        if not line:
            in_decode_area = False
            continue
        line = line.strip()
        if in_decode_area:
            lsplits = line.split()
            if len(lsplits) == 1 and value is not None:
                value += lsplits[0]
            elif len(lsplits) == 3:
                if key is not None:
                    dataset_features.update({key: value})
                key = lsplits[1].rstrip(':?')
                value = lsplits[2]
        # Catch start of feature description area
        if line.startswith('7. Attribute Information'):
            in_decode_area = True
    dataset_features.update({key: value})
    # Load data
    df = pd.read_csv(data_file, encoding='UTF-8', names=dataset_features)
    # Build and return Dataset
    return Dataset(**dataset_info, features=dataset_features, data=df)
