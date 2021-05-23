import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())
print(ufo.columns)

#pass rename columns keyword arguement, pass coloumns dictionary with \
#  original column name in key and new column name in value
ufo.rename(columns = {'Colors Reported': 'Colors_Reported'})

ufo.rename(columns = {'Colors Reported': 'Colors_Reported'}, inplace=True)
#use in place keyword argument to change columns in place \
#ie change the original dataframe

print(ufo.columns) #to check


#another way
#create list of new columns and save to variable
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols

print(ufo.columns)

#one more method
ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols, header=0)
#use names and header keyword arguments