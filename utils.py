from pymongo import MongoClient


def getDB():
    client = MongoClient()
    db = client.users
    return db

def authorize(username, password):
    user = db.Collections.find_one({'username':username, 'password':password})
    if user:
        return 0
    else:
        return None

def addUser(username, password):
##    db.insert(user: 'username', password: 'password')
    db = getDB()
    temp = db.find_one({'username': username}, fields= {'_id': False})
    if temp == None:
        db.insert({'username' : username, 'password': password 'events': []})
        return True
    else:
        return False


def checkUser(username):
#returns t if the user already exists
    db = getDB()
    temp = db.find_one({'username': username}, fields = {'_id' : False})
    if temp == None:
        return False
    else: 
        return True


def checkPass(username, password):
#Function required for login. Check that the password works. Returns t if logs in.
    db = getDB()
    temp = db. find_one({'username': username, 'password': password})
    if temp == None:
        return False
    else:
        return True
    
    

def changePass(username, oldpass, newpass):
#Change the user's password, maintain username.
    db = getDB()
    if checkPass(username, oldpass):
        db.update({'username': username}, {'$set': {'password': newpass}})
        return True
    else:
        return False
