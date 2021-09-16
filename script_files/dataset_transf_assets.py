# <pep8-80 compliant>

import pandas as pd

# reading from models table in Helga, converted to CSV
df = pd.read_csv("models.csv")

# show_id 14 only relates to Project Tube
project_tube_only = (df['show_id'] == 14)


cleanup_dict = {'Characters': ['Character', 'character', 'Secondary character', 
                               'background character', 'crowd character', 'ch'],
                'Environment': ['Set', 'set', 'setprop'],
                'Props': ['props', 'prop', 'Prop', 'cards', 'Cloth'],
                'Python Scripts': ['python script'],
                'Software': ['software'],
                'Vehicles': ['Vehicle', 'vehicle']
                }


def filter_chains(cases, desired_word):

    head = "((df['type'] == '"
    mid = "') | (df['type'] == '"
    tail = "'))"

    filter_query = project_tube_only & eval(head + mid.join(cases) + tail)
    df.loc[filter_query, 'type'] = desired_word


for desired_word, cases in cleanup_dict.items():
    filter_chains(cases, desired_word)


df.rename(columns={'name': 'Name',
                   'type': 'Type',
                   'description': 'Description'},
          inplace=True)


final_df = df.loc[project_tube_only, ['Type', 'Name', 'Description']]
final_df.set_index('Type', inplace=True)

final_df['Name'] = final_df['Name'].apply(
    lambda s: str(s).capitalize().replace('_', ' ').strip())
final_df['Description'] = final_df['Description'].apply(
    lambda s: str(s).capitalize().replace('Nan', '').strip())


final_df.to_csv('assets_import_payload.csv')
