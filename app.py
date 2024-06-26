from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import requests, csv, argparse
from urllib.request import urlopen

### flask server ###

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# endpoint for the home landing page
# cross_origin() must be used for CORS headers for the API request
@app.route("/")
@cross_origin()
def home():

    url = "https://api-web.nhle.com/v1/schedule/now"

    resp = requests.get(url)
    data = resp.json()
    items = len(data['gameWeek'][0]['games'])
    return render_template("home.html", value=data, length=items)

# endpoint for the leaders page. returns 2 arrays of data
@app.route("/leaders")
@cross_origin()
def leaders():

    goals_url = "https://api.nhle.com/stats/rest/en/leaders/skaters/goals?cayenneExp=season=20232024"

    goals_resp = requests.get(goals_url)
    goals_data = goals_resp.json()

    assists_url = "https://api.nhle.com/stats/rest/en/leaders/skaters/assists?cayenneExp=season=20232024"
    
    assists_resp = requests.get(assists_url)
    assists_data = assists_resp.json()

    return render_template("leaders.html", goals=goals_data, assists=assists_data)

# default endpoint for the players page
@app.route("/players")
@cross_origin()
def search():

    url = "https://api-web.nhle.com/v1/player/8479407/landing"
    resp = requests.get(url)
    data = resp.json()

    return render_template("players.html", value=data)

# endpoint for the standings page
@app.route("/standings")
@cross_origin()
def getStandings():

    url = "https://api-web.nhle.com/v1/standings/now/"
    resp = requests.get(url)

    data = resp.json()

    return render_template("standings.html", value=data)

# endpoint for the about page
@app.route("/about")
def getAbout():
    return render_template("about.html")

# endpoint for the schedule page
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
    player_id = getPlayerID(data['value'])

    if (player_id == 0):
        return jsonify(result = 0)

    # remove the new line escape sequence from the string 
    player_id = player_id.strip('\n')

    url = "https://api-web.nhle.com/v1/player/" + player_id + "/landing"

    resp = requests.get(url)

    if (resp.status_code == 404):
        print("an error occurred")
    info = resp.json()

    return jsonify(result=info)

# function to get and return the id based on the players name
def getPlayerID(player):

    player = player.upper()

    id = {}    
    # open and read a text file with player ids 
    with open('players.txt', 'r') as player_ids:
        data = player_ids.readlines()
    
    # search through the file and find the requested player name then store the id
    for line in data:
        if player in line:
            # split the players id from the player name
            id = line.rsplit(' ', 1)

    # if the player id does not exist, return a 0
    if (len(id) != 2):
        id[1] = 0
        return id[1]

    return id[1]

# use this to run server locally on port 5000 (by default)
if __name__ == "__main__":
    app.run(debug=True)
