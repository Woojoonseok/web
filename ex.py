# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:56:42 2020

@author: Seokwoojoon
"""
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
     'author': {
         'username' : 'test-user'
         },
     'title':'Test',
     'content':'네즈코',
     'date_posted': datetime.strptime('2020-02-01', '%Y-%m-%d')
     },
    {
     'author': {
         'username' : 'test-user'
         },
     'title':'Test_2',
     'content':'네즈코_2',
     'date_posted': datetime.strptime('2020-02-01', '%Y-%m-%d')
     }
]

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html', posts = posts)

@app.route("/about")
def about():
	return render_template('about.html', title = 'About')


if __name__ == "__main__":
	app.run('0.0.0.0', port=5000)
    
