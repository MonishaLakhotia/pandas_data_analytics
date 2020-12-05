import pdfplumber
from py_linq import Enumerable
import toml
import os
import pandas_data_analytics.utils as u
from pandas_data_analytics.text_parser.parser import Parser
import re

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

u.set_full_paths(config, this_dir)
pdf_loc = config['file_locations']['data']

parser_settings = toml.load(os.path.join(this_dir, 'pdf_config.toml'))
parser = Parser(parser_settings)


def merge_dicts(d1, d2):
    # dicts must have the exact same keys
    # if values from d1 are None, then use d2's value
    d3 = {}
    for k, v in d1.items():
        if v is None or v == '':
            d3[k] = d2[k]
        else:
            d3[k] = v
    return d3


with pdfplumber.open(pdf_loc) as pdf:
    result = Enumerable(pdf.pages)\
        .select(lambda page: page.extract_text())\
        .select(parser.parse)\
        .aggregate(merge_dicts)
    print(result)
