from flask import Flask, request,render_template
import json
import urllib,urllib2

app=Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
        
@app.route("/login", methods = ["GET", "POST"])
def login():
## THIS MAY OR MAY NOT BE A REAL FLASK THING
    if request.method == "GET":
            return render_template("login.html")
    else:
        username = input.get("username")
        password = input.get("password")
        if username in session:
            return "Logged in as " + username
        else:
            if checkPass(username, password)
        

@app.route("/search")
def search():
    return render_template("search.html")
    


@app.route("/results")
def res():
    return render_template("results.html")


@app.route("/share")
def share():
    return render_template("share.html")


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)






