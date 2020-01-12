#Code for NDVI calculation
#Note it is just NDVI calculation and the NDVI values are calculated per pixel.
from rasterio.windows import Window
import rasterio as rio
import  matplotlib.pyplot as plot
import numpy as np
from rasterio.plot import show

src = rio.open(r"C:\Users\divya\OneDrive\Desktop\Satnaoutput.tif")
print("Band count is",src.count)
red = src.read(2, window=Window(0,0,3182,1703)).astype(np.float) 
print("Band 3 Matrix",red)
nir = src.read(3, window=Window(0,0,3182,1703)).astype(np.float)
print("Band 4 Matrix",nir) 
red[red == src.nodata] = np.nan  # Convert NoData to NaN
nir[nir == src.nodata] = np.nan  # Convert NoData to NaN
#Red Band displaying  
fig1 = plot.imshow(red)
fig1.set_cmap('Reds')
plot.title("Band 3 : Red Band")
plot.show()
#NIR Band displaying
fig2 = plot.imshow(nir)
fig2.set_cmap('nipy_spectral')
plot.title("Band 4 : NIR Band")
plot.show()
#NDVI calculation
ndvi = (nir - red) / (nir + red)
vmin, vmax = np.nanpercentile(ndvi, (1,99))  # 1-99% contrast stretch
img_plt = plot.imshow(ndvi, cmap="gray",vmin=vmin, vmax=vmax)
plot.title("NDVI")
plot.show()
print("NDVI values :",ndvi)