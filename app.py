from flask import Flask, request, render_template, url_for, redirect, session, request
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
    if request.form.get("password_register","")==request.form.get("confirmpassword_register",""):
        #createUser will return a number depending on what the error was
        result=utils.createUser(request.form.get("username_register","").lower(),request.form.get("password_register",""))
        #success. Login page will have confirmation message
        if result==0:
            return render_template("home.html",type_register=0)
            #username is already taken
        elif result==1:
            return render_template("home.html",type_register=1)
            #username or pw is invalid
        else: 
            return render_template("home.html",type_register=2)
        #pw mismatch
    else:
        return render_template("home.html",type_register=3)
        
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

@app.route("/makeevent")
def makeevent():
    if "username" not in session:
	    return redirect("home")
    if request.method=="POST":
        result = {"location" : str(request.form.get("event_location",""),)
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
    app.run(host='0.0.0.0',port=8000)






