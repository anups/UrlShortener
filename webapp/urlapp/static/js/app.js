
$(document).ready(function(){
    timestamp = []
    data = $('#expired_at').val();
    console.log(data)
    if (data !== undefined) {
        hours = data.split(":")[0].split(" ")[3]
        minutes = data.split(":")[1].split(" ")[0]
        median = data.split(":")[1].split(" ")[1]
        if (median == "p.m."){
            hours = parseInt(hours) + 12
        }
        timestamp.push(hours)
        timestamp.push(minutes)
        console.log(timestamp);
        var d = new Date($.now());
        var minutes_now = d.getMinutes()
        var hours_now = d.getHours()
        console.log(hours_now, minutes_now);
        if (parseInt(hours_now) > parseInt(hours)){
            $("a").removeAttr('href');
        }
        else if (parseInt(minutes_now) == parseInt(timestamp[1]) || parseInt(minutes_now) > parseInt(timestamp[1])){
            $("a").removeAttr('href');
        }
    }
});
