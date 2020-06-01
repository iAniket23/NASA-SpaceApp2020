"""
That file downloads the specified data from LAADCS DAAC 2020 resources of the DNB VIIRS sensor

In order to use, wget must be installed on your pc
"""

import os, urllib, urlencode


# The SUBFOLDER variable decides which subfolder to download from 2020 folder.
# As an indication, by now (31st of may 2020), there is 152 subfolders that
# represent all data from january 1st 2020 till now.

# In that script, we'll download only subfolders 070 to 130, that covers the area
# of march 10th to may 10th.

# That my personnal key I got from LAADS DAAC registration
API_PERSONNAL_KEY = "YOUR_API_KEY"

def downloadfiles():
    subfolder = int(70)
    while 70 <= subfolder <= 130:
        if subfolder < 100:
            os.system('wget -e robots=off -m -np -R .html,.tmp -nH --cut-dirs=3 f"https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ103DNB/2020/0{subfolder}/" --header f"Authorization: Bearer {API_PERSONNAL_KEY}"') 
            subfolder += 1

        else:
            os.system('wget -e robots=off -m -np -R .html,.tmp -nH --cut-dirs=3 f"https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ103DNB/2020/{subfolder}/" --header f"Authorization: Bearer {API_PERSONNAL_KEY}"')
            subfolder += 1


if __name__ == '__main__':
    downloadfiles()
