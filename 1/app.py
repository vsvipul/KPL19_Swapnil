from flask import Flask,render_template,redirect,url_for,request
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')         #starting the index template



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u

nu=[]
for i in range(275):
    nu.append(str(i))
@app.route('/mid',methods = ['POST','GET'])         #function to check the input id of the stars
def mid():
	if request.method == 'POST':
		usd=(request.form['fname'])
		if usd in nu:
			return redirect(url_for('success',messages=usd))     #redirect to the success function to find closest star
		else:
		    return 'INVALID STAR ID'

@app.route('/success')
def success():                                          
    columns = ['id','ra','dec','long','lat','spec_rs','photo_rs','photo_rs_e','dist','ci']      #changing the column name
    df=pd.read_csv('./data.csv')                                # reading the csv file
    df.columns = columns


    def get_stars(idx):
        row = df.loc[df['id'] == idx]
        ra1 = row.ra.values[0]
        dec1 = row.dec.values[0]
        coord1 = SkyCoord(ra=ra1*u.degree,dec=dec1*u.degree,frame='gcrs')
        #print(ra1,dec1)
        #print(coord1)
        return coord1

    distcord = []                                               #list of angle separation and 
    c1 = get_stars(int(request.args.get('messages')))

    for i in range(1,274):
        c2 = get_stars(i)
        sep = c1.separation(c2)                                     #finding angle separation 
        distcord.append(([sep,(df['ra'][i],df['dec'][i])]))
       
    distcord.sort(key=lambda x:x[0])                                #sorting the stars
    #print(distcord[0][0])
    for j in range(1,6):                            #5 closest id's
     print(j,"Coordinate",distcord[j][1])
    return render_template('re.html',messages=distcord)
if __name__ == '__main__':                                          #hosting the app on this port
   app.run(host = '0.0.0.0', port = 7000)