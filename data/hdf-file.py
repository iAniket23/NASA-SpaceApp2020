
import pandas as pd

hdf = pd.HDFStore('../../desktop/datafile.h5', mode='r')

hdf = hdf.keys()

print(hdf)