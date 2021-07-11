from flask import Flask

@app.route("/")
@app.route("/home")
def home():
    return('First test page')
