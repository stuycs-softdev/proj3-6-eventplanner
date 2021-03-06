from flask import Flask, request, render_template, url_for, redirect, session, request
import json
import urllib,urllib2
import yelp
import utils

app=Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



@app.route("/")
def home():
        if "username" not in session:
                return render_template("index.html")
        else:
                return redirect("/search")


@app.route("/register", methods = ["GET", "POST"])
def register():
    if "username" in session:
    	return redirect(url_for("search"))
    if request.method == "GET":
        return render_template("register.html")
    if "username" not in session:
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]
        securityq = request.form["securityq"]
        securitya = request.form["securitya"]
        if utils.register(username, password, confirm, securityq, securitya):
            session["username"] = username
            return redirect(url_for("search"))
        else:
             return redirect(url_for("register"))
    else:
         return redirect(url_for("search"))

        
@app.route("/login", methods = ["GET", "POST"])
def login():
    if "username" in session:
    	return redirect(url_for("search"))
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if utils.authorize(username, password):
            session["username"] = username
            return redirect(url_for("search"))
        else:
            return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/")

        

@app.route("/search", methods = ["GET", "POST"])
def search():
    if request.method == "GET":
	return render_template("search.html")
    keyword = request.form['keyword']
    location = request.form['location']
    session["results"] =  yelp.search(keyword, location)
    return redirect("/results")
    


@app.route("/results")
def results():
    if "results" not in session:
        return redirect("search")
    else:
        return render_template("results.html", username=session["username"], results=session["results"])


@app.route("/share")
def share():
    return render_template("share.html")

@app.route("/makeevent", methods = ["GET", "POST"])
def makeevent():
    if "username" not in session:
	    return redirect(url_for("login"))
    elif "results" not in session:
        return redirect(url_for("search"))
    elif request.method=="POST":
        event = {"location" : request.form['location'],
		  "date" : request.form['date'],
		  "time" : request.form['time'],
		  "attendees" : [session["username"]]}
	for key in event:
	    if event[key] == None:
		return redirect(url_for("makeevent"))    
        utils.addEvent(session["username"],event)    
        return render_template("profile.html")
    else:
        return render_template("makeevent.html", results=session["results"])
        
@app.route("/profile")
def profile():
    events = utils.getEvents(session["username"])
    return render_template("profile.html", username = session['username'], events = events)


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)






