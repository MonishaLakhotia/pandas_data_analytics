import pandas_data_analytics.utils as u
import toml
from pandas_data_analytics import *
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import functools as ft
import sqlite3

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'config.toml'))

u.set_full_paths(config, this_dir)
db_loc = config['file_locations']['data']

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect(db_loc)
query = """
SELECT 
s.Description
, q.questiontext
, a.*
FROM Answer AS a
LEFT JOIN Survey AS s ON s.SurveyID = a.SurveyID
LEFT JOIN Question AS q on q.QuestionID = a.QuestionID
"""

rs = con.execute("""
SELECT DISTINCT
COUNT(QuestionID)
FROM Answer
GROUP BY SurveyID
""")

for r in rs:
  print(r)

df = pd.read_sql_query(query, con)

# Apply the default theme
sns.set_theme()

# plt.show()
