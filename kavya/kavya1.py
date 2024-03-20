from flask import Flask 

app=Flask(__name__)

a=10
b=20

@app.route('/',methods=['GET']) 
def welcome():
    return 'hello world'

@app.route('/login',methods=['GET'])
def login():
    return 'you are in login page'
