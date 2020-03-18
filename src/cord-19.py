import numpy as np
import pandas as pd

sources = pd.read_csv('data/raw/2020-03-13/all_sources_metadata_2020-03-13.csv')

sources.describe()

print(sources)