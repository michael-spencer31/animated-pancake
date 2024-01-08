from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def home():

    url = "https://api-web.nhle.com/v1/schedule/now"

    resp = requests.get(url)
    data = resp.json()
    away = data['gameWeek'][0]['games'][0]['homeTeam']['placeName']['default']
    items = len(data['gameWeek'][0]['games'])
    return render_template("home.html", value=data, length=items)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

