from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

plantType = "Wind"
code = '518'

lat, lon = [], []
f = open(sys.argv[1], 'rb')
rowCount = 0
try:
    reader = csv.reader(f)
    for row in reader:
        #if row[26] != '' and row[15] == plantType:
        #if row[26] != '' and row[10] == code:
        if row[63] != '' and rowCount != 0:
            lat.append(float(row[63]))
            lon.append(float(row[64]))
        rowCount += 1
        # if row[26] != '':
        #     lat.append(float(row[26]))
        #     lon.append(float(row[27]))
finally:
    f.close()

# create polar stereographic Basemap instance.
m = Basemap(projection='stere',lon_0=-95,lat_0=90.,
            llcrnrlat=20, urcrnrlat=49,
            llcrnrlon=-115, urcrnrlon=-63,
            rsphere=6371200., resolution='h', area_thresh=10000)
# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawcounties()
m.drawrivers(color="blue")
# draw parallels.
parallels = np.arange(0., 90, 10.)
m.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=10)
# draw meridians
meridians = np.arange(180., 360., 10.)
m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=10)
# compute native map projection coordinates of lat/lon grid.
x, y = m(lon, lat)
m.plot(x, y, 'ro', markersize=6)
# add title
plt.title("Power Plant Locations - " + plantType)
plt.show()
