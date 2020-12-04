import pdfplumber
from py_linq import Enumerable
import toml
import os
import pandas_data_analytics.utils as u

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

u.set_full_paths(config, this_dir)
pdf_loc = config['file_locations']['data']

with pdfplumber.open(pdf_loc) as pdf:
    all_txt = Enumerable(pdf.pages).aggregate(lambda acc, page: acc+page.extract_text(), "")
