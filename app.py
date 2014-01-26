from flask import Flask, request,render_template
import json
import urllib,urllib2
import yelp
import utils

app=Flask(__name__)



@app.route("/")
def home():
        if "username" not in session:
                return render_template("index.html")
        else:
                return redirect("/search")


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
        
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method=="POST":
        result = utils.authorize(str(request.form.get("username_login","")).lower(), str(request.form.get("password_login","")))
        #successful login
	if result == 0:  
            session["username"] = request.form.get("username_login","")
            return redirect("/route")
        #failed attempt!
        else:
            return render_template("home.html",type_login=1)
    else:
        return render_template("home.html")

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/")

        

@app.route("/search")
def search():
    start = request.form.get("1","")
    end = request.form.get("2","")
    if start == None or end == None:
        return render_template("route.html")
    try:
        results = yelp.search(food, location)
    except KeyError:
        return render_template("route.html")
    session["results"] = results
    return redirect("results")
    


@app.route("/results")
def results():
    if "results" not in session:
        return redirect("route")
    else:
        return render_template("results.html", results=session["results"])


@app.route("/share")
def share():
    return render_template("share.html")


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)






