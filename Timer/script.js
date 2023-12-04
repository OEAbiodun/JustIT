  // Set the date we're counting down to
let countDownDate = new Date("Dec 31, 2023 00:00:00").getTime();

  // Update the countdown every 1 second
let x = setInterval(function() {

    // Get the current date and time
    let now = new Date().getTime();

    // Calculate the remaining time
    let distance = countDownDate - now;

    // Calculate days, hours, minutes, and seconds
    let days = Math.floor(distance / (1000 * 60 * 60 * 24));
    let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the countdown in the "countdown" element
    document.getElementById("countdown").innerHTML = days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";

    // If the countdown is over, display a message
    if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "EXPIRED";
    }
}, 1000);