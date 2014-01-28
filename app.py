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
     if request.method == "GET":
         return render_template("register.html")

     elif not utils.loggedIn():
         username = request.form["username"]
         password = request.form["password"]
         confirm = request.form["confirm"]
         securityq = request.form["securityq"]
         securitya = request.form["securitya"]

         if utils.register(username, password, confirm, securityq, securitya):
             return redirect(url_for("home"))
         else:
             return redirect(url_for("register"))
     else:
         return redirect(url_for("home"))

        
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    elif not utils.loggedIn():
        username = request.form["username"]
        password = request.form["password"]
        if utils.authorize(username, password):
            session["username"] = username
            return redirect(url_for("search"))
        else:
            return redirect(url_for("home"))

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
        return render_template("results.html", results=session["results"])


@app.route("/share")
def share():
    return render_template("share.html")

@app.route("/makeevent")
def makeevent():
    if "username" not in session:
	    return redirect("home")
    if request.method=="POST":
        result = {"location" : str(request.form.get("event_location","")),
		  "date" : str(request.form.get("event_date","")),
		  "time" : str(request.form.get("event_time","")),
		  "attendees" : [session["username"]]}
	for key in result:
	    if result[key] == None:
		return redirect("makeevent")    
            else:
		utils.addEvent(result)    
                return render_template("profile.html")
    else:
        return render_template("makeevent.html")
        
@app.route("/profile")
def profile():
    events = utils.getEvents(session["username"])
    return render_template("profile.html", username = session['username'], events = events)


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)






