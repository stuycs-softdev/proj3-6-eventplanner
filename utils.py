from pymongo import MongoClient


def getDB():
    client = MongoClient()
    db = client.users
    return db


def addUser(username, password):
    db = getDB()
##    db.insert(user: 'username', password: 'password')


def checkUser(username):
#returns t or f if the user already exists
    db = getDB()

def checkPass(username, password):
#Function required for login. Check that the password is 

def changePass(username, oldpass, newpass):
#Change the user's password, maintain username.


