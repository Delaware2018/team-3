# Author: Lela Bones
# This document creates the instance of the app and runs it

import os, os.path
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map



# creates instance of the class Flask
app = Flask(__name__)
GoogleMaps(app)

@app.route("/map_loc")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=39.1582786,
        lng= -75.5433835,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 39.60655499999999,
             'lng': -75.71021300000001,
             'infobox': "<b>Bear</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 38.7364091,
             'lng': -75.5936,
             'infobox': "<b>Bridgeville</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
             'lat': 39.8516208,
             'lng': -75.44341800000001,
             'infobox': "<b>Chadds Ford</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/orange-dot.png',
             'lat': 39.835988,
             'lng': -122.1400,
             'infobox': "<b>Chichester</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
             'lat': 39.7946645,
             'lng': -75.46801770000002,
             'infobox': "<b>Claymont</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 39.1582786,
             'lng': -75.5433835,
             'infobox': "<b>Dover-Gateway Shopping Center</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
             'lat': 39.1265445,
             'lng': -75.53303740000001,
             'infobox': "<b>Dover-Rodney Village</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 39.9709756,
             'lng': -75.30266440000003,
             'infobox': "<b>Havertown</b>"
          },
        ]
    )
    return render_template('map_loc.html', mymap=mymap, sndmap=sndmap)


# locally creates a page
@app.route('/')
def index():
    # loads the template home
    return render_template('home.html')

@app.route('/donations')
def donations():
    #loads the template donations
    return render_template('donations.html')

@app.route('/purchases')
def purchases():
    #loads the template donations
    return render_template('purchases.html')

@app.route('/rewards')
def rewards():
    #loads the template donations
    return render_template('rewards.html')

@app.route('/impact')
def impact():
    #loaffs the template impact
    return render_template('impact.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']  != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# locally creates a page
@app.route('/about')
def about():
    # load the template about
    return render_template('about.html')
    
# locally creates a page
@app.route('/help')
def help():
    return render_template('help.html')

# locally creates a page
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# locally creates a page
@app.route('/thankyou')
def thankyou():
    # load the template about
    return render_template('thankyou.html')

# locally creates a page
@app.route('/thankyouF')
def thankyouF():
    # load the template about
    return render_template('thankyouF.html')

if __name__ == '__main__':
    # runs app in debug mode
        app.run(port=5000, debug=True)
# app.run()