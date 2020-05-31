import gdal, os

## List input HDF4 files, change it to your own directory
os.chdir('C:\\Users\guill\Desktop\HDF4')

rasterFiles = os.listdir(os.getcwd())
print(rasterFiles)

#Get File Name Prefix
rasterFilePre = rasterFiles[0][:-4]
print(rasterFilePre)

fileExtension = ".tif"

## Open HDF file (first if multiple files are in same directory)
hdflayer = gdal.Open(rasterFiles[0], gdal.GA_ReadOnly)

#print (hdflayer.GetSubDatasets())

# Open raster layer
#hdflayer.GetSubDatasets()[0][0] - for first layer
#hdflayer.GetSubDatasets()[1][0] - for second layer ...etc
rlayer = gdal.Open(hdflayer.GetSubDatasets()[1][0], gdal.GA_ReadOnly)
outputName = rlayer.GetMetadata_Dict()['long_name']


outputNameNoSpace = outputName.strip().replace(" ","_").replace("/","_")
outputNameFinal = outputNameNoSpace + rasterFilePre + fileExtension
print(outputNameFinal)

outputFolder = "C:\\OutputFolder\\"

outputRaster = outputFolder + outputNameFinal

gdal.Warp(outputRaster,rlayer)


#Display image in QGIS (run it within QGIS python Console) - remove comment to display
#iface.addRasterLayer(outputRaster, outputNameFinal)