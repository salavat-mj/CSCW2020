## source ./conda/bin/activate
from pathlib import Path
import pandas as pd
import numpy as np


columns = ['ID', 'URL', 'Designer', 'Company_Name', 'Date', 'Tags', 'Views', 'Likes', 'Saves', 'Comments', 'Attachments', 'Title', 'Description', 
           13, 14, 15, 16, 17, 18, 19, 20]

## Read
data = pd.read_csv(
    "Metadata.csv", 
    encoding= 'CP866', 
    low_memory=False, 
    names=columns,
    thousands=',',
    index_col='ID',
    # parse_dates=['date'],
    )

## Description
# data['Description'] = data \
#     .loc[:, 'Description':] \
#     .fillna('') \
#     .agg(' '.join, axis=1) \
#     .replace({'        ': np.nan})
# data = data.loc[:, :'Description']

data.tail()

## ID
path = Path('./Dribbble_test/website/')
id = [int(p.stem) for p in path.glob('Images/*')]
id

## Tags
tags = data.loc[id, 'Tags'].str.strip().str.replace('   ', ',')
tags

## Save
for number, current_tags in tags.items():
    with open(f'./{path}/Tags/{number}.txt', 'w+') as f:
        f.write(current_tags)