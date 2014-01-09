from pymongo import MongoClient


def getDB():
    client = MongoClient()
    db = client.users
    return db


def addUser(username, password):
    db = getDB()
##    db.insert(user: 'username', password: 'password')


def checkUser():
#returns t or f
    db = getDB

def checkPass():


def changePass():



