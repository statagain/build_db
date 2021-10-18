import re
import pandas as pd
from scipy.io.arff import loadarff
from .core import get_working_dir, Dataset

dataset_info = {
    'id_': 'UCI_ML_00602',
    'short_name': 'dry_bean',
    'name': 'Dry Bean Dataset',
    'url': 'https://archive.ics.uci.edu/ml/datasets/Dry+Bean+Dataset',
    'attribution':
        'Murat KOKLU, Faculty of Technology, Selcuk University, TURKEY. '
        'Ilker Ali OZKAN, Faculty of Technology, Selcuk University, TURKEY.',
    'desc':
        'Images of 13,611 grains of 7 different registered dry beans '
        'were taken with a high-resolution camera. A total of 16 features; '
        '12 dimensions and 4 shape forms, were obtained from the grains.'
}


def load_dry_beans():
    dataset_id = dataset_info['id_']
    dataset_dir = get_working_dir() / f'{dataset_id}'
    desc_file = dataset_dir / f'{dataset_id}.desc'
    data_file = dataset_dir / f'{dataset_id}.data'
    # Load data
    with open(data_file, 'r') as f:
        data, _ = loadarff(f)
    df = pd.DataFrame(data)
    df['Class'] = df['Class'].apply(lambda x: x.decode('ascii'))
    # Get features from description
    with open(desc_file, 'r') as f:
        dataset_desc = f.read()
    feature_desc = []
    for line in dataset_desc.splitlines():
        if re.match(r'\d+\.\)', line):
            feature_desc.append(
                ''.join(line.split(")", maxsplit=1)[1]).strip())
    features = dict(zip(df.columns, feature_desc))
    # Build and return Dataset
    return Dataset(**dataset_info, features=features, data=df)
