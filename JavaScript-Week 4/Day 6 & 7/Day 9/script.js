// //time and date

// let count = 0;
// function greeting(name) {
//     console.log(`Hello, How are you ${name}?`);
//     count++;
//     if (count == 3)
//     {
//         clearInterval(interval);
//     }
// }
// // setTimeout(greeting, 10000, 'Bootcamp');
// let three = setTimeout(greeting, 3000, 'Bootcamp');
// let five = setTimeout(greeting, 5000, 'All')
// clearTimeout(three);

// //setInterval()

// setInterval(greeting, 3000, 'All');

// let interval = setInterval(greeting, 3000, 'All');


// let k = 0;

// function greet(name) {
//     if (k < 10) {
//         k++;
//         console.log(k);
//         if (k == 10) {
//             console.log(`Calling of Function is now cancelled. ${name}`);
//             clearInterval(interval);
//         }
//     }
// }
// let interval = setInterval(greet, 3000, 'Hurray!');



let date = new Date();
console.log(date);
console.log('Current time: ', date);

let date1 = new Date(2023, 0, 19);
console.log(date1);

let date2 = new Date().toLocaleString('en-US', {timeZone:'Asia/Kabul'})
console.log(date2);
let date3 = new Date().toLocaleString('en-US', {timeZone:'Africa/Lagos'})
console.log("Lagos Time: " , date3);

let localDate = date.toLocaleDateString('en-uk',{month: 'long', day: '2-digit', year: 'numeric', weekday: 'long'});
console.log('Another way', localDate);

console.log(date.getDate());

let day = "th";

let localDate1 = date.toLocaleDateString('en-uk',{ weekday: 'long', day: '2-digit', month: 'long' , year: 'numeric',});
console.log('Assignment', localDate);


function liveWatch(){
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();

let sess = "AM"

if (hh===0){
    hh = 12;
}
if (hh > 12){
    hh = hh - 12;
    sess = "PM";
}
hh = (hh < 10) ? "0" + hh : hh;
mm = (mm < 10) ? "0" + mm : mm;
ss = (ss < 10) ? "0" + ss : ss;


let time = hh + ":" + mm + ":" + ss + "" + sess;
document.getElementById("date").innerText = time;
let t = setTimeout(function(){ liveWatch()}, 1000);
}

liveWatch();
// function greet(name) {
//     if (k < 20) {
//         k++;
//         console.log(k);
//         if (k == 20) {
//             console.log(`Calling of Function is now cancelled. ${name}`);
//             clearInterval(interval);
//         }
//     }
// }
// let inter = setInterval(greet, 3000, 'Hurray!');



