"""
Copies of selected statistical and ML datasets used in the StatAgain project,
with code required to load and merge them into a sqlite database.
"""

__title__ = __name__
__description__ = __doc__.replace('\n', ' ').replace('\r', '').strip()
__version__ = '0.2.1'
__author__ = 'Aleksandr Mikhailov'
__author_email__ = 'avidclam+statagain@gmail.com'
__copyright__ = '2022, Aleksandr Mikhailov'

from .core import init_db
from .uci_ml_00579 import load_MI_complications
from .uci_ml_00602 import load_drybeans
from .ggplot2_diamonds import load_diamonds