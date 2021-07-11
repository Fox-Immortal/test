from test import app

if __name__ == '__main__': 
    app.run(debug=True)

@app.route("/")
@app.route("/home")
def home():
    return('First test page')