from flask import Flask, request,render_template
import json
import urllib,urllib2

app=Flask(__name__)



@app.route("/")
def home():




@app.route("/register")
def register():


@app.route("/login")
def login():

@app.route("/search")
def search():


@app.route("/results")
def res():


@app.route("/share")
def share():


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)






