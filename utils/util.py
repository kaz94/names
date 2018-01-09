import os
from pathlib import Path

from utils.constants import DATA_DIR


def get_data_dir():
    return Path(os.getenv(DATA_DIR, None))


