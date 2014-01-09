from flask import Flask, request,render_template
import json
import urllib,urllib2

app=Flask(__name__)



@app.route("/")
def home():




@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
        
@app.route("/login", methods = ["GET", "POST"])
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






