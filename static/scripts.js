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