""" Python HDF File Reader Canvas"""

# Must install 'pandas' and 'tables' for it to work
import pandas as pd

# Change the directory to file location
hdf = pd.read_hdf('sample-datafile.h5', mode='r')

"""
Other useful panda outputs:

pd.read_table()
pd.read_csv()
pd.read_excel()
pd.ExcelFile.parse()
pd.read_json()

pd.HDFStore.put()
pd.HDFStore.get()
pd.HDFStore.select()
pd.HDFStore.keys()
"""


if __name__ == '__main__':
    #print(hdf)
    hdf.head()