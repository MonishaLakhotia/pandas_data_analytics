from pandas_preprocessor import *
import os
import toml

this_dir = os.path.dirname(os.path.realpath(__file__))
config_name = "config.toml"

# Loads config
tomlLoc = os.path.join(this_dir, config_name)
config = toml.load(tomlLoc)

# prefix all file locations with this directory
set_full_paths(config, this_dir)
# Loads pickled model
model = load_model(config)

# get user query
df = get_dataframe(config['input_query'])

# clean user query for models consumption
house_data = df.drop(['Address', 'Method', 'SellerG', 'Date',
                      'Postcode', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], axis=1)
house_data = clean_input(house_data, config['dataframe'])
outputColumnNames = [o['name'] for o in config['dataframe']['outputs']]
house_to_value = house_data.drop(outputColumnNames, axis=1)

print('Cleaned DF')
print(house_data.head())

# ask the model the user query
predicted_house_value = model.predict(house_to_value)

predicted_house_value = predicted_house_value[0]

# Print estimated value of the property to two decimal places
print("This property has an estimated value of AUD %.2f" %
      predicted_house_value)

# Transform user query back to users data structure
inverted_house_data = invert_cleaning(house_data, config['dataframe'])

print('Inverted DF')
print(inverted_house_data.head())
