from flask import Flask, request,render_template
import json
import urllib,urllib2
import yelp

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
## THIS MAY OR MAY NOT BE A REAL FLASK THING
    if request.method=="GET":
                return render_template("login.html")
        username = request.form['name']
        password = request.form['password']
        print username
        print password
        if not username or not password:    
                return render_template("login.html", message = "Please fill out the empty fields!")
        elif utils.checkPass(username, password): 
                session["username"] = username
                return redirect("/search")
        else:
                return render_template("login.html", message = "Incorrect username and password combination.")

        

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
    return render_template("results.html")


@app.route("/share")
def share():
    return render_template("share.html")


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)






