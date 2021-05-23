import pyodbc
from pandas_data_analytics import *
from py_linq import Enumerable
import matplotlib.pyplot as plt
import os
import pandas as pd
import src.utils as u
import re
import seaborn as sns
import toml

this_dir = os.path.dirname(os.path.realpath(__file__))
config = toml.load(os.path.join(this_dir, 'data', 'config.toml'))
# connection string is of a generic form
# Ex: con_str="Driver={SQL Server};Server=server_name;Database=database_name;Trusted_Connection=yes;"
conn = pyodbc.connect(config['con_str'])

sql_query = 'SELECT TOP(10) * FROM EDIProvider'
df: pd.DataFrame = pd.read_sql_query(sql_query, conn)

print(df.head())
print(df.shape)

# cursor = conn.cursor()
# cursor.execute(sql_query)

# for row in cursor:
#     print(row)
