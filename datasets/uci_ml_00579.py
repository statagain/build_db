import pandas as pd
from .core import get_working_dir, Dataset

dataset_info = {
    'id_': 'UCI_ML_00579',
    'short_name': 'MI_complications',
    'name': 'Myocardial infarction complications Data Set',
    'url': 'https://archive.ics.uci.edu/ml/datasets/'
           'Myocardial+infarction+complications',
    'attribution': 'S.E. Golovenkin, V.A. Shulman, D.A. Rossiev, '
                   'P.A. Shesternya, S.Yu. Nikulina, Yu.V. Orlova: Professor '
                   'V.F. Voino-Yasenetsky Krasnoyarsk State Medical University;'
                   ' A.N. Gorban, E.M. Mirkes: University of Leicester.',
    'desc': 'The proposed database can be used to solve two practically '
            'important problems: predicting complications of Myocardial '
            'Infarction (MI) based on information about the patient '
            '(i) at the time of admission and '
            '(ii) on the third day of the hospital period. '
            'Columns 2-112 can be used as input data for prediction. '
            'Possible complications (outputs) are listed in columns 113-124.'
}


def load_MI_complications():
    units = ['mmHg', 'mmol/L', 'IU/L', 'Ð¼Ð¼']
    dataset_id = dataset_info['id_']
    dataset_dir = get_working_dir() / f'{dataset_id}'
    desc_file = dataset_dir / f'{dataset_id}.desc'
    data_file = dataset_dir / f'{dataset_id}.data'
    # Get features from description
    features = {}
    with open(desc_file, 'r') as f:
        dataset_desc = f.read()
    in_decode_area = False
    for line in dataset_desc.splitlines():
        if line == 'List of attributes':
            in_decode_area = True
        elif line.startswith('0: unknown (alive)'):
            in_decode_area = False
        if in_decode_area:
            lsplits = line.split('(')
            if len(lsplits) > 1:
                if any(lsplits[-1].startswith(unit) for unit in units):
                    # last braketed token is a unit, not feature name
                    rsplits = lsplits[-2].split(')')
                else:
                    rsplits = lsplits[-1].split(')')
                if len(rsplits) > 1:
                    name = rsplits[0]
                    if ' ' not in name:
                        features[name] = ''.join(line.split('.')[1:]).strip()
    # Load data
    df = pd.read_csv(data_file, sep=',', header=None, names=features,
                     na_values='?')
    # Build and return Dataset
    return Dataset(**dataset_info, features=features, data=df)
