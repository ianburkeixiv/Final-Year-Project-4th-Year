from flask import Flask, render_template, request 
import requests
# Pass in __name__ to help flask determine root path
app = Flask(__name__) # create the application instance

# Routing/Mapping
# @ signifies a decorator which is a way to wrap a function and modify its behaviour
@app.route('/') #connect a webpage. '/' is a root directory.
def main():
    return render_template("index.html")

@app.route('/temputure', methods=['POST']) #connect a webpage. '/' is a root directory.
def temputure():
    req = request.get('http://api.openweathermap.org/data/2.5/weather?&APPID=a662d25dc808bf3a512b5aab0cbfa6e2&q=galway')
    json_object = req.json()
    temp = float(json_object['main']['temp'])
    
    return render_template("index.html", temp=temp)

@app.route('/dashboard') #connect a webpage. '/' is a root directory.
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True) # Start the web app. debug=True means to auto refresh page after code changes 