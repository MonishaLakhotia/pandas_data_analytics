import src.utils as u
import re
import toml
from src import *
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import functools as ft
from py_linq import Enumerable
from glob import glob

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))
u.set_full_paths(config, this_dir)
csv_loc = config['file_locations']['raw_el_pollo_loco']

files = sorted(glob(os.path.join(this_dir, 'all_data/cleaned_data/*.csv')))
df = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)
df.columns = df.columns.str.lower()

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)

ps = (lambda pdf: Enumerable([
  lambda: pdf.columns,
  lambda: pdf.sample(10),
]))(df)
u.foreach(lambda f: print(f()), ps)

df.to_csv(config['file_locations']['clean_all_data'], index=False)
