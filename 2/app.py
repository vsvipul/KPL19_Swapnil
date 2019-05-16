from dustmaps.sfd import SFDQuery
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord
import matplotlib.pyplot as plt
import pandas as pd
import astropy.units as u
df=pd.read_csv('./data.csv')

for i in df['Column 9']:
    i = (10**((i+5)/5))/1000

c = []
c1 = []
for i in range(1,274):
    c.append(coord.ICRS(ra=df['Column 2'][i]*u.degree,dec=df['Column 3'][i]*u.degree,distance=df['Column 9'][i]*u.kpc))


for i in range(1,273):
    c1.append(c[i].transform_to(coord.Galactocentric))
print(c1)

plt.plot(df['Column 7'],df['Column 9'])
plt.show()