from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import requests, csv, argparse

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

    goals_url = "https://api.nhle.com/stats/rest/en/leaders/skaters/goals?cayenneExp=season=20232024"

    goals_resp = requests.get(goals_url)
    goals_data = goals_resp.json()

    assists_url = "https://api.nhle.com/stats/rest/en/leaders/skaters/assists?cayenneExp=season=20232024"
    
    assists_resp = requests.get(assists_url)
    assists_data = assists_resp.json()

    return render_template("about.html", goals=goals_data, assists=assists_data)

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

@app.route("/schedule")
@cross_origin()
def getSchedule():

    return render_template("schedule.html")

@app.route('/getSchedule', methods=['POST'])
@cross_origin()
def get_games():

    data = request.get_json()
    url = data['value']
    
    resp = requests.get(url)
    info = resp.json()

    return jsonify(result=info)

@app.route('/process', methods=['POST'])
@cross_origin()
def process():
    data = request.get_json()
    player_id = getPlayerName(data['value'])

    player_id = player_id.strip('\n')

    url = "https://api-web.nhle.com/v1/player/" + player_id + "/landing"
    print(url)
    resp = requests.get(url)
    info = resp.json()

    return jsonify(result=info)

def getPlayerName(player):

    player = player.upper()

    with open('players.txt', 'r') as player_ids:
        data = player_ids.readlines()
    
    for line in data:
        if player in line:
            print(line)
            id = line.rsplit(' ', 1)
            
    return id[1]


if __name__ == "__main__":
    app.run(debug=True)

