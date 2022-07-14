import pandas as pd
from .core import get_working_dir, Dataset


dataset_info = {
    'id_': 'ggplot2_diamonds',
    'name': 'diamonds',
    'title': 'Prices of over 50,000 round cut diamonds',
    'url': 'https://ggplot2.tidyverse.org/reference/diamonds.html',
    'attribution': 'Hadley Wickham',
    'description':
        'A dataset containing the prices and other attributes of almost '
        '54,000 diamonds.'
}


dataset_features = {
    'price': 'price in US dollars ($326-$18,823)',
    'carat': 'weight of the diamond (0.2-5.01)',
    'cut': 'quality of the cut (Fair, Good, Very Good, Premium, Ideal)',
    'color': 'diamond colour, from D (best) to J(worst)',
    'clarity': 'a measurement of how clear the diamond is '
               '(I1(worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(best))',
    'x': 'length in mm(0 - 10.74)',
    'y': 'width in mm(0 - 58.9)',
    'z': 'depth in mm(0 - 31.8)',
    'depth': 'total depth percentage = '
             'z / mean(x, y) = 2 * z / (x + y) (43 - 79)',
    'table': 'width of top of diamond relative to widest point(43 - 95)'
}


def load_diamonds():
    dataset_id = dataset_info['id_']
    dataset_dir = get_working_dir() / f'{dataset_id}'
    data_file = dataset_dir / f'{dataset_id}.csv'
    # Load data
    df = pd.read_csv(data_file, encoding='UTF-8')
    correct_column_sequence = list(dataset_features.keys())
    # Build and return Dataset
    return Dataset(**dataset_info,
                   features=dataset_features,
                   data=df.filter(correct_column_sequence))
