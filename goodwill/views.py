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

@app.route("/locations")
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
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('locations.html', mymap=mymap, sndmap=sndmap)
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
def help_page():
    return render_template('help.html')


if __name__ == '__main__':
    # runs app in debug mode
        app.run(port=5000, debug=True)
        # app.run()
  
