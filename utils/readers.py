from pathlib import Path
import os

import pandas as pd
import re


def read(file: Path):
    names_df = pd.read_table(file, header=None, delimiter=',')
    names_df.columns = ['name', 'sex', 'quantity']
    names_df['year'] = re.findall(r'\d+', str(file))[0]

    return names_df


def read_by_state(file: Path):
    names_df = pd.read_table(file, header=None, delimiter=',')
    names_df.columns = ['code', 'sex', 'year', 'name', 'quantity']

    return names_df


def join_files(directory: str):
    joint = pd.DataFrame()
    for file in os.listdir(directory):
        joint = joint.append(read(Path(directory) / file), ignore_index=True)

    return joint


# print(read(Path('/home/kasia/PycharmProjects/names/data/usa/names/yob1950.txt')))