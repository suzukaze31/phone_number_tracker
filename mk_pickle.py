import pandas as pd

pd.read_csv('phone_numbers.csv', names=['address', 'outer', 'inner']).to_pickle('phone_numbers_data.pickle')
