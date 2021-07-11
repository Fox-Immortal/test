from flask import Flask
from test import app

@app.route("/")
@app.route("/home")
def home():
    return('First test page')
