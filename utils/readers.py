from pathlib import Path
import os

import pandas as pd
import re


def read(file: Path):
    names_df = pd.read_table(file, header=None, delimiter=',')
    names_df.columns = ['name', 'sex', 'quantity']
    names_df['year'] = re.findall(r'\d+', str(file))[0]

    return names_df


def read_us_by_state(file: Path):
    names_df = pd.read_table(file, header=None, delimiter=',')
    names_df.columns = ['code', 'sex', 'year', 'name', 'quantity']

    return names_df


def read_france_by_dep(file: Path):
    names_df = pd.read_table(file, header=0, delimiter='\t', encoding='ISO-8859-1')
    names_df.columns = ['sex', 'name', 'year', 'code', 'quantity']

    return names_df


def read_files(directory: str, read_func):
    joint = pd.DataFrame()
    for file in os.listdir(directory):
        joint = joint.append(read_func(Path(directory) / file), ignore_index=True)

    return joint


def read_sweden(data_dir: Path, files: list):
    names_df = pd.DataFrame()
    for file in files:
        names_df = names_df.append(pd.read_csv(data_dir / file, header=4), ignore_index=True)

    return names_df


def read_england(data_dir: Path, files: list):
    names_df = pd.DataFrame()
    for file in files:
        names_df = names_df.append(pd.read_csv(data_dir / file, header=[4, 5]), ignore_index=True)

    return names_df


# print(read(Path('/home/kasia/PycharmProjects/names/data/usa/names/yob1950.txt')))