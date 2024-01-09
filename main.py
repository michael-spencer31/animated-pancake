from flask import Flask, render_template, jsonify, request
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
    items = len(data['gameWeek'][0]['games'])
    return render_template("home.html", value=data, length=items)

@app.route("/about")
@cross_origin()
def about():

    url = "https://api-web.nhle.com/v1/standings/now"

    resp = requests.get(url)
    data = resp.json()

    return render_template("about.html", value=data)

@app.route("/info")
@cross_origin()
def info():

    url = "https://api-web.nhle.com/v1/player/8479407/landing"
    resp = requests.get(url)
    data = resp.json()

    return render_template("info.html", value=data)

@app.route("/standings")
@cross_origin()
def getStandings():

    url = "https://api-web.nhle.com/v1/standings/now"
    resp = requests.get(url)

    data = resp.json()

    return render_template("standings.html", value=data)

@app.route('/process', methods=['POST'])
@cross_origin()
def process():
    data = request.get_json()
    player_id = getPlayerName(data['value'])

    url = "https://api-web.nhle.com/v1/player/" + player_id + "/landing"

    resp = requests.get(url)
    info = resp.json()

    return jsonify(result=info)

def getPlayerName(player):

    player = player.upper()

    player_dict = {
        "SIDNEY CROSBY": "8471675",
        "KRIS LETANG": "8471724",
        "NICK SUZUKI": "8480018",
        "COLE CAUFIELD": "8481540",
        "FILIP MESAR": "8483488"
    }
    return player_dict[player]


if __name__ == "__main__":
    app.run(debug=True)

