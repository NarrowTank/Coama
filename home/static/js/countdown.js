const daysEl = document.getElementById("days")
const hoursEl = document.getElementById("hours")
const minutesEl = document.getElementById("minutes")
const secondsEl = document.getElementById("seconds")

const contador = "20 jun 2024 12:00:00";


function countdown(){
    //const timeZone = "UTC";
    const contadorDate = new Date(contador);
    const currentDate = new Date();

    const totalSeconds = (contadorDate - currentDate) / 1000;

    const days = Math.floor(totalSeconds / 3600 / 24);
    const hours = Math.floor(totalSeconds / 3600) % 24;
    const minutes = Math.floor(totalSeconds / 60) % 60;
    const seconds = Math.floor(totalSeconds ) % 60;

    daysEl.innerHTML = days;
    hoursEl.innerHTML = formatTime (hours);
    minutesEl.innerHTML = formatTime (minutes);
    secondsEl.innerHTML = formatTime (seconds);

}

function formatTime(time){
    return time < 10 ? `0${time}` : time;
}

countdown();

setInterval(countdown, 1000);