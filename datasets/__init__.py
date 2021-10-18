"""
Copies of some statistical and ML datasets used in the StatAgain project,
with code required to etl them into a single sqlite database.
"""

__title__ = __name__
__description__ = __doc__.replace('\n', ' ').replace('\r', '').strip()
__version__ = '0.1.0'
__author__ = 'Aleksandr Mikhailov'
__author_email__ = 'am@statagain.ru'
__copyright__ = '2021, Aleksandr Mikhailov'

from .core import init_db
from .uci_ml_00579 import load_MI_complications
from .uci_ml_00602 import load_dry_beans