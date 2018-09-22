# Author: Lela Bones
# This document creates the instance of the app and runs it

import os, os.path
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory


# creates instance of the class Flask
app = Flask(__name__)

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
    #loads the template impact
    return render_template('impact.html')

# locally creates a page
@app.route('/about')
def about():
    # load the template about
    return render_template('about.html')

# locally creates a page
@app.route('/form')
def form():
    # load the template about
    return render_template('form.html')

# locally creates a page
@app.route('/create_account')
def create_account():
    # load the template about
    return render_template('create_account.html')

# locally creates a page
@app.route('/form_purchase')
def form_purchase():
    # load the template about
    return render_template('form_purchase.html')
    
# locally creates a page
@app.route('/help')
def help_page():
    return render_template('help.html')


if __name__ == '__main__':
    # runs app in debug mode
        app.run(port=5000, debug=True)
        # app.run()
  
