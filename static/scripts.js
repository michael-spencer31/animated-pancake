//function to convert UTC time to users local time zone
function convertTime (data, num) {

    var utc = data.gameWeek[0]['games'][num]['startTimeUTC'];
    var date = new Date(utc);
    var local_time = new Date(date.toString());
    var start24 = local_time.getHours() + ":" + local_time.getMinutes() + "0";

    return start24;   
}

function getGoalie (goalie) {


}

function getSchedule (response, past_day) {
    console.log("Hello, World!");
}

function overallPick (round, pick, year) {

    // if it is the first round, just return the pick number
    if (round == 1) {
        return getNumberWithOrdinal(pick);
    } else {

        if (year <= 2000) {
            return getNumberWithOrdinal((round - 1) * 28 + pick);
        // before 2016: 30 NHL teams
        } else if (year <= 2016 && year > 2000) {
            return getNumberWithOrdinal((round - 1) * 30 + pick);
            // 2017 - 2021 Vegas gets added, 31 NHL teams
        } else if (year >= 2017 && year <= 2021) {
            return getNumberWithOrdinal((round - 1) * 31 + pick);
        }
        // 2021 - now Seattle gets added 32 NHL teams
        return getNumberWithOrdinal((round - 1) * 32 + pick);
    }
}

function getNumberWithOrdinal (n) {

    var s = ["th", "st", "nd", "rd"], v = n % 100;

    return n + (s[(v - 20) % 10] || s[v] || s[0]);
}
function convertAbrv(team) {

    const team_names = new Map([
        ["COL", "Colorado"],
        ["MTL", "Montréal"],
        ["BOS", "Boston"],
        ["CAR", "Carolina"],
        ["CBJ", "Columbus"],
        ["TOR", "Toronto"],
        ["CGY", "Calgary"],
        ["LAK", "Los Angeles"],
        ["EDM", "Edmonton"],
        ["DAL", "Dallas"],
        ["DET", "Detriot"],
        ["MIN", "Minnesota"],
        ["NJD", "New Jersey"],
        ["STL", "St. Louis"],
        ["SJS", "San Jose"],
        ["VAN", "Vancouver"],
        ["TBL", "Tampa Bay"],
        ["WIN", "Winnipeg"],
        ["NSH", "Nashville"],
        ["WSH", "Washington"],
        ["SEA", "Seattle"],
        ["VGK", "Vegas"],
        ["PHI", "Philadelphia"],
        ["NYR", "Rangers"],
        ["NYI", "Islanders"],
        ["ATL", "Atlanta"],
        ["BUF", "Buffalo"],
        ["CHI", "Chicago"],
        ["PIT", "Pittsburgh"],
        ["ARI", "Arizona"],
        ["OTT", "Ottawa"],
    ]);
    return team_names.get(team);
}

function getCountry (city, country) {

    const countries = new Map([
        ["CAN", "Canada"],
        ["USA", "United States"],
        ["SWE", "Sweden"],
        ["FIN", "Finland"],
        ["RUS", "Russia"],
    ]);
    return city + ", " + countries.get(country);
}