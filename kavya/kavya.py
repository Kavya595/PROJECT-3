from flask import Flask 

app=Flask(__name__)


@app.route('/',methods=['GET']) 
def welcome():
    return 'i can perform  maths ops'

@app.route('/sub/<a>/<b>',methods=['GET'])
def substraction(a,b):
    a=int(a)
    b=int(b)
    return f"substraction of {a} and {b} is {a-b}"

@app.route('/add/<a>/<b>',methods=['GET'])
def addition(a,b):
    a=int(a)
    b=int(b)
    return f"addition of {a} and {b} is {a+b}"

@app.route('/multiply/<a>/<b>',methods=['GET'])
def multiply(a,b):
    a=int(a)
    b=int(b)
    return f"product of {a} and {b} is {a*b}"

@app.route('/division/<a>/<b>',methods=['GET'])
def division(a,b):
    a=int(a)
    b=int(b)
    return f"division of {a} and {b} is {a//b}"

app.run()